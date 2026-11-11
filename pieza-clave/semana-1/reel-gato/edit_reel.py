"""Edita el reel del gato: python3 edit_reel.py A|B salida.mp4"""
import subprocess, sys, os
R=os.path.dirname(os.path.abspath(__file__))
V, OUT = sys.argv[1], sys.argv[2]
END='/home/user/Claude-movil/pieza-clave/semana-1/posts/mie-2-cierre-reel-anuncio.png'
# (archivo, inicio dentro del clip, duración, overlay)
SEG=[('clips/v1.mp4',0.6,2.2,f'ov/hook{V}.png'),
     ('clips/v2.mp4',0.4,3.8,'ov/t2.png'),
     ('clips/v3.mp4',0.3,4.0,'ov/t3.png'),
     ('clips/v4.mp4',0.5,2.8,'ov/t4.png')]
ENDDUR=2.7
def run(a): subprocess.run(a,check=True,cwd=R)
parts=[]
for i,(clip,ss,d,ov) in enumerate(SEG):
    out=f'tmp_s{i}.mp4'; parts.append(out)
    run(['ffmpeg','-y','-v','error','-ss',str(ss),'-t',str(d),'-i',clip,'-loop','1','-t',str(d),'-i',ov,
         '-filter_complex',
         '[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,'
         'eq=contrast=1.04:saturation=1.06[b];'
         f'[1:v]format=rgba,fade=in:st=0.12:d=0.18:alpha=1[o];[b][o]overlay=0:0:format=auto,format=yuv420p[v]',
         '-map','[v]','-an','-c:v','libx264','-preset','medium','-crf','18','-r','30',out])
# cierre: imagen con zoom lento
n=int(ENDDUR*30)
run(['ffmpeg','-y','-v','error','-loop','1','-i',END,'-t',str(ENDDUR),'-filter_complex',
     f"[0:v]scale=2160:3840,zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps=30,format=yuv420p[v]",
     '-map','[v]','-c:v','libx264','-preset','medium','-crf','18','tmp_end.mp4'])
parts.append('tmp_end.mp4')
open(f'{R}/tmp_list.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i','tmp_list.txt','-c','copy','tmp_video.mp4'])
total=sum(s[2] for s in SEG)+ENDDUR
sfx_at=int((SEG[0][2]+SEG[1][2]+0.25)*1000)
run(['ffmpeg','-y','-v','error','-i','tmp_video.mp4','-i','audio/music.mp3','-i','audio/sfx.mp3','-filter_complex',
     f'[1:a]atrim=0:{total},afade=t=out:st={total-0.7}:d=0.7,volume=0.85[m];'
     f'[2:a]adelay={sfx_at}|{sfx_at},volume=14dB[s];[m][s]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]',
     '-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',OUT])
for p in parts+['tmp_video.mp4','tmp_list.txt']: os.remove(os.path.join(R,p))
print('ok',OUT,round(total,2),'s')
