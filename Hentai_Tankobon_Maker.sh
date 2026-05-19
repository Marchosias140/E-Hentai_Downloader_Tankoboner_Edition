#!/bin/bash

Downloading () {

E-Hentai_Downloader

sleep 2s

convert-cbz -input ./Scraped_Images -output ./CBZ_File

rm -r ./Scraped_Images

}

Renaming () {

read -r -p "Input file name " variable1

mv ./CBZ_File/Scraped_Images.cbz ./CBZ_File/$variable1.cbz

}

Downloading

Renaming
