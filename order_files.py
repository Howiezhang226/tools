#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
video_postfix = ("mp4", "wmv", "mov","mkv","avi")
doc_postfix = ("pdf", "PDF", "docx","doc","xlsx", "ppt", "pptx", "DOCX","txt")
music_postfix = ("mp3", "ape", "flac", "amr")
book_postfix = ("epub", "mobi")
pic_postfix = ("jpg", "JPG", "png", "PNG")
archive_postfix = ("rar", "zip", "dmg", "DMG", "pkg")
root_path = "/Users/haozhang/Downloads/"

target_video_dir = root_path + "video"
target_doc_dir = root_path + "document"
target_torrent_dir = root_path + "torrent"
target_music_dir = root_path + "music"
target_book_dir = root_path + "book"
target_pic_dir = root_path + "picture"
target_archive_dir = root_path + "archive"

def move_file(source_dir, target_dir):
    try:
        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)
        shutil.move(source_dir, target_dir)
        log = "move " + source_dir + " to " + target_dir
        with open("/Users/haozhang/Desktop/log/log.txt", 'a') as log_file:
            log_file.write(log + '\n')
    except Exception as e:
        raise


for root, dir, files in os.walk("/Users/haozhang/Downloads"):
    for file in files:
        if root == "/Users/haozhang/Downloads":
            file_path = os.path.join(root, file)
            if file_path.endswith(video_postfix):
                move_file(file_path, target_video_dir)
            if file_path.endswith(doc_postfix):
                move_file(file_path, target_doc_dir)
            if file_path.endswith("torrent"):
                move_file(file_path, target_torrent_dir)
            if file_path.endswith(music_postfix):
                move_file(file_path, target_music_dir)
            if file_path.endswith(book_postfix):
                move_file(file_path, target_book_dir)
            if file_path.endswith(pic_postfix):
                move_file(file_path, target_pic_dir)
            if file_path.endswith(archive_postfix):
                move_file(file_path, target_archive_dir)
