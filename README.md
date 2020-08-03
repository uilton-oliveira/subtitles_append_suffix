# subtitles_append_suffix
Append suffix to subtitles files, useful to add language suffix to all subtitles, to be recognized by Plex, for example.  
It will recursively scan all files and subfolders to SUBTITLE_RENAME_DIR

Docker run example:  
```sh
docker run -it --rm \  
    -v "F:\Media\Series:/rename/series_local1" \  
    -v "E:\Media\Series:/rename/series_local2" \  
    -v "F:\Media\Filmes:/rename/filmes_local1" \  
    -v "E:\Media\Filmes:/rename/filmes_local2" \  
    -e SUBTITLE_RENAME_DIR=/rename \  
    -e SUBTITLE_SUFFIX=.pt \  
    -e SUBTITLE_EXT=.srt \  
    uilton/subtitles_append_suffix:latest sh
```
