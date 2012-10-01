#!/bin/sh
OUTPUT=../files/usr/share/cinnamon/locale/es/LC_MESSAGES/cinnamon.mo
INPUT=cinnamon_cinnamon-es.po

msgfmt "$INPUT" -o "$OUTPUT"
