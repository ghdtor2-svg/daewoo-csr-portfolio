#!/usr/bin/env python3
"""Render editable JSON and the existing template as a static Netlify site."""
from pathlib import Path
from html import escape
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public'


def text(value):
    if not isinstance(value, str):
        raise ValueError('문자열을 입력해 주세요.')
    return escape(value, quote=True)


def image_path(value):
    path = ROOT / value
    if not value.startswith('assets/images/') or not path.resolve().is_relative_to((ROOT / 'assets/images').resolve()) or not path.is_file():
        raise ValueError(f'이미지 파일을 찾을 수 없습니다: {value}')
    return text(value)


def render_project(project, number):
    title = text(project['title'])
    category = text(project['category'])
    identity = project['id']
    if not re.fullmatch(r'[a-z0-9-]+', identity):
        raise ValueError('사업 id에는 영문 소문자, 숫자, 하이픈을 사용해 주세요.')
    if project.get('image'):
        alt = text(project.get('imageAlt') or project['title'])
        media = f'''<div class="relative h-56 overflow-hidden bg-slate-200">
          <img src="{image_path(project['image'])}" alt="{alt}" loading="lazy" data-lightbox class="w-full h-full object-cover cursor-pointer hover:scale-105 transition duration-500">
          <div class="absolute top-3 left-3 bg-brand-700 text-white text-xs px-2.5 py-1 rounded-md font-medium">{category}</div>
        </div>'''
    else:
        media = f'''<div class="relative h-56 bg-gradient-to-br from-brand-900 to-navy-900 flex flex-col items-center justify-center text-white p-6">
          <div class="absolute top-3 left-3 bg-brand-600 text-white text-xs px-2.5 py-1 rounded-md font-medium">{category}</div>
          <i data-lucide="store" class="w-12 h-12 text-teal-300 mb-3" aria-hidden="true"></i>
          <p class="text-3xl font-extrabold">{text(project.get('metric', project['title']))}</p>
          <p class="text-sm text-teal-100 mt-2">{title}</p>
        </div>'''
    fields = []
    for field in project['fields']:
        color = 'text-brand-700 font-semibold' if field.get('highlight') else 'text-slate-600'
        fields.append(f'''<div class="flex items-start gap-2"><span class="font-semibold text-slate-700 min-w-[40px]">{text(field['label'])}:</span><span class="{color}">{text(field['value'])}</span></div>''')
    video = ''
    if project.get('video'):
        info = project['video']
        video_id = info['id']
        if not re.fullmatch(r'[A-Za-z0-9_-]{11}', video_id):
            raise ValueError('YouTube 영상 ID는 11자리입니다.')
        video = f'''<div class="mt-4 pt-3 border-t border-slate-200">
          <div class="flex items-center justify-between mb-2 gap-2">
            <span class="text-xs font-bold text-slate-700">{text(info['title'])}</span>
            <a href="https://www.youtube.com/watch?v={video_id}" target="_blank" rel="noopener noreferrer" class="text-xs text-red-600 font-semibold">YouTube에서 열기</a>
          </div>
          <div class="relative w-full aspect-video rounded-xl overflow-hidden shadow-md border border-slate-200 bg-black">
            <iframe src="https://www.youtube.com/embed/{video_id}" title="{text(info['title'])}" loading="lazy" class="absolute top-0 left-0 w-full h-full border-0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
          </div>
        </div>'''
    return f'''<article id="{identity}" class="bg-slate-50 border border-slate-200 rounded-2xl overflow-hidden card-hover flex flex-col">
      {media}
      <div class="p-6 flex-1">
        <h3 class="text-xl font-bold text-slate-900 mb-2">{number}. {title}</h3>
        <div class="space-y-2 mb-4 text-sm">{''.join(fields)}</div>
        <div class="bg-white p-4 rounded-xl border border-slate-200 text-xs text-slate-600 leading-relaxed mb-4"><strong>상세내용:</strong> {text(project['description'])}</div>
        {video}
      </div>
    </article>'''


def main():
    site = json.loads((ROOT / 'content/site.json').read_text(encoding='utf-8'))
    projects = json.loads((ROOT / 'content/projects.json').read_text(encoding='utf-8'))
    if not projects:
        raise ValueError('사업을 하나 이상 입력해 주세요.')
    ids = [project['id'] for project in projects]
    if len(ids) != len(set(ids)):
        raise ValueError('사업 id가 중복되었습니다.')
    values = {key: text(value) for key, value in site.items()}
    values['projectCount'] = str(len(projects))
    values['projects'] = '\n'.join(render_project(project, i + 1) for i, project in enumerate(projects))
    template = (ROOT / 'templates/index.html').read_text(encoding='utf-8')
    rendered = re.sub(r'\{\{(\w+)\}\}', lambda match: values[match[1]], template)
    # Validate all local photo references before replacing previous output.
    for source in re.findall(r'<img[^>]*src="([^"]+)"', rendered):
        image_path(source)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / 'assets', OUT / 'assets')
    (OUT / 'index.html').write_text(rendered, encoding='utf-8')
    print(f'빌드 완료: public/index.html (사업 {len(projects)}개)')


if __name__ == '__main__':
    main()
