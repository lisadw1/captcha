#!/bin/bash

LOCAL_DIR="/kaggle/working/dddd_trainer/projects/ocr1/models"

for file in "${LOCAL_DIR}"/*; do
  if [ -f "$file" ]; then
    echo "File: $(basename "${file}")"
  fi
done
