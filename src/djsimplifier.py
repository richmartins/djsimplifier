#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class DjSimplifer:
    urls: list = []
    save_path: str = ""

    def __init__(self, urls, save_path) -> None:
        # self.urls = [tuple(url.items())[0]) for url in urls]
        self.urls = [tuple(url.items())[0] for url in urls]

        self.save_path

    def hooker(d):
        print(d['status'])
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    def download(self) -> bool:
        print(self.urls)
        for url in self.urls:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'logger': MyLogger(),
                'progress_hooks': [self.hooker],  # lol
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            }

            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url[1]])
            except Exception as e:
                raise Exception(f"error with url: {url}\nException: {e}")
