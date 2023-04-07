#!/usr/bin/env bash

#set -x

nbdev_clean --clear_all

GIT_STATUS_FAILED(){
  git status -uno -s |grep '.*\.ipynb'
}

if GIT_STATUS_FAILED; then
  echo "!! ::error:: Detected notebooks that are not cleaned."
  false;
fi
