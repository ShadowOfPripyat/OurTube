from cement import Controller, ex
from pytube import YouTube
import os

class Downloads(Controller):
    class Meta:
        label = 'download videos'
        stacked_type = 'embedded'
        stacked_on = 'base'

    @ex(
        help="download only one video",
        arguments=[
            (['video_link'],{
                'help': 'link of the video you want to download',
                'action': 'store'
            }),
            (['--path'],{
                'help': 'the path where the video will be saved',
                'action': 'store',
                'dest': 'path'
            }),
            (['--format'], {
                'help': 'the format you want to download (mp4 or mp3)',
                'action': 'store',
                'dest': 'format'
            })
        ]
    
    )
    def download(self):
        link = self.app.pargs.video_link
        path = self.app.pargs.path
        download_format = self.app.pargs.format
        video = YouTube(link)
        if download_format == 'mp4':
            try:
                stream = video.streams.get_highest_resolution()
                self.app.log.info('Working...')
                stream.download(output_path=path)
                self.app.log.info('video successfully downloaded!')
                self.app.log.info(f'path: {path}')
            except:
                self.app.log.error('Not a valid YouTube URL')
            
        
        elif download_format == 'mp3': 
            stream = video.streams.filter(only_audio=True).first()
            try:
                self.app.log.info('Working...')
                out_file = stream.download(path)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                self.app.log.info('audio of the given video successfully downloaded!')
                self.app.log.info(f'path: {path}')
            except:
                self.app.log.error('Not a valid YouTube URL')