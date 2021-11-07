# You-get

### 使用方式

​	最简单的使用命令就是`you-get + 完整的视频URL`，例如：

```python
you-get https://v.youku.com/v_show/id_XMzk4NDE2Njc4OA==.html?firsttime=0
```



#### 常用指令

| 选项 |                            说明                            |
| :--: | :--------------------------------------------------------: |
|  -i  |          显示资源信息，比如说格式、清晰度、大小等          |
|  -u  |      指定下载或查看的url，有时候可以省略-u直接加上url      |
|  -o  | 设置输出文件夹，即保存路径，若不指定，则保存在当前工作目录 |
|  -O  |                设置文件名，可采用默认文件名                |
|  -l  |                      优先下载整个列表                      |
|  -P  |                使用密码（若访问视频需要密码                |
|  -t  |                   设置超时时间，单位是秒                   |
|  -c  |       使用cookie，加载cookies.txt 或者cookies.sqlite       |
|  -f  |                    强制覆盖已存在的文件                    |

​	

例如获取视频的清晰度信息：

```
C:\Users\panme>you-get -i https://v.youku.com/v_show/id_XMzk4NDE2Njc4OA==.html?spm=a2hcb.playlsit.page.3
site:                优酷 (Youku)
title:               序章：罗网之心
streams:             # Available quality and codecs
    [ DEFAULT ] _________________________________
    - format:        mp4hd2v2
      container:     mp4
      video-profile: 超清
      size:          408.0 MiB (427772864 bytes)
      m3u8_url:      http://pl-ali.youku.com/playlist/m3u8?vid=XMzk4NDE2Njc4OA&type=mp4hd2v3&ups_client_netip=&utid=IH39Fw7t71ICAXjlXg%2Fhl3Gi&ccode=0519&psid=0acded556dae2a5e0feaa495f793d1e543162&duration=1836&expire=18000&drm_type=1&drm_device=7&hotvt=1&dyt=0&btf=&rid=20000000AB6DED846DCB7C159A8F5F1F9D5B8C1102000000&ups_ts=1601605412&onOff=0&encr=0&ups_key=805dd73f9545b034dcc6a7a69b732fbd
    # download-with: you-get --format=mp4hd2v2 [URL]

    - format:        mp4hd
      container:     mp4
      video-profile: 高清
      size:          240.0 MiB (251650734 bytes)
      m3u8_url:      http://pl-ali.youku.com/playlist/m3u8?vid=XMzk4NDE2Njc4OA&type=mp4hdv3&ups_client_netip=&utid=IH39Fw7t71ICAXjlXg%2Fhl3Gi&ccode=0519&psid=0acded556dae2a5e0feaa495f793d1e543162&duration=1836&expire=18000&drm_type=1&drm_device=7&hotvt=1&dyt=0&btf=&rid=20000000DDB7A0907D7D8F79B3ABDB846BFC24AF02000000&ups_ts=1601605412&onOff=0&encr=0&ups_key=21d750ed3dc71da20f0c7cb8445d9952
    # download-with: you-get --format=mp4hd [URL]

    - format:        3gphd
      container:     mp4
      video-profile: 渣清
      size:          61.5 MiB (64509670 bytes)
      m3u8_url:      http://pl-ali.youku.com/playlist/m3u8?vid=XMzk4NDE2Njc4OA&type=3gphdv3&ups_client_netip=&utid=IH39Fw7t71ICAXjlXg%2Fhl3Gi&ccode=0519&psid=0acded556dae2a5e0feaa495f793d1e543162&duration=1836&expire=18000&drm_type=1&drm_device=7&hotvt=1&dyt=0&btf=&rid=20000000445FB791872AA862408C9EDF7E5C66B302000000&ups_ts=1601605412&onOff=0&encr=0&ups_key=4723945818c1e89b0d04b070bc72230b
    # download-with: you-get --format=3gphd [URL]

    - format:        mp4sd
      container:     mp4
      video-profile: 标清
      size:          125.4 MiB (131501709 bytes)
      m3u8_url:      http://pl-ali.youku.com/playlist/m3u8?vid=XMzk4NDE2Njc4OA&type=flvhdv3&ups_client_netip=&utid=IH39Fw7t71ICAXjlXg%2Fhl3Gi&ccode=0519&psid=0acded556dae2a5e0feaa495f793d1e543162&duration=1836&expire=18000&drm_type=1&drm_device=7&hotvt=1&dyt=0&btf=&rid=20000000D6EF6F9992D1E2D38FCFF05CC4C4E5A002000000&ups_ts=1601605412&onOff=0&encr=0&ups_key=97cf235b2d0672159d024defe04565a5
    # download-with: you-get --format=mp4sd [URL]

```



发现它有4种画质，它默认是给我们下载最高画质的视频，这次我们让它下载最低画质的视频，并且指定保存的路径和重命名文件。

```python
you-get --format=3gphd https://v.youku.com/v_show/id_XMzk4NDE2Njc4OA==.html?spm=a2hcb.playlsit.page.3 -o C:\Users\panme\Desktop\ -O 罗网之心.mp4

```



