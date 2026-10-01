# Oil × NatGas 101 联合学习

网站：https://jaheadfour.github.io/oil-gas-learning/

七段、35 站的中文油气交错学习课程，包含 Oil 101 V3、NatGas 101、图例、知识树与中英对照。
学习进度仅存在各设备的浏览器中。

## 发布

完整静态网站以分片 ZIP 保存；`site-parts.json` 记录每片及完整 ZIP 的 SHA-256。
GitHub Actions 运行 `unpack_site.py` 验证并还原完整目录，然后发布 `public/` 到 GitHub Pages。
分片仅用于浏览器上传大小限制，网站访问时不需要下载或解压。

课程原始来源、图片出处与历史数据边界见各课正文。
