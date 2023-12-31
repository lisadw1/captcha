#!/bin/bash

LOCAL_DIR="/kaggle/working/dddd_trainer/projects/ocr1/models"
WEBDAV_URL="https://wani.teracloud.jp/dav"
USERNAME="dawda"
PASSWORD="DpS5H3jzA9VxF8hr"

# 创建当前时间戳文件夹名称
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
REMOTE_DIR="${WEBDAV_URL}/${TIMESTAMP}"

# 使用MKCOL方法创建WebDAV远程文件夹
curl -X MKCOL -u "${USERNAME}:${PASSWORD}" "${REMOTE_DIR}"

for file in "${LOCAL_DIR}"/*; do
  if [ -f "$file" ]; then
    remote_file="${REMOTE_DIR}/$(basename "${file}")"
    curl -T "${file}" -u "${USERNAME}:${PASSWORD}" "${remote_file}"
  fi
done

remote_file1="${REMOTE_DIR}/1.zip")"
curl -T "${file}" -u "${USERNAME}:${PASSWORD}" "${remote_file1}"
