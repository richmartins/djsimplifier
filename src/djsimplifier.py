#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import youtube_dl


class Djsimplifer:
    urls: list = []

    def __init__(self, urls) -> None:
        self.urls = urls

    def download(self) -> bool:
        for url in self.urls:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
            except:
                raise (f"error with: {url}")

    def check_dependencies(self) -> bool:
        ...
