# shell 基础语法
---
## ls
### ls：列出当前文件夹的内容。
### ls -a：列出当前文件夹的内容（包括隐藏文件）。
- 隐藏文件：以'.'开头的文件。
  1. '.' 当前文件夹。
  2. '..' 上一级文件夹。
  3. '.aa' 名字为'.aa'的文件或文件夹。
- 非隐藏文件文件：其他文件。

## cd
打开某某文件夹。

## mv
### mv a.txt b.txt 将a.txt文件重命名为b.txt文件
### mv a/c.txt b/c.txt 将a文件夹中的c.txt文件移动到b文件夹中，名字仍为c.txt
### mv a/c.txt b/d.txt 将a文件夹中的c.txt文件移动到d文件夹中，名字更改为d.txt

## mkdir xx
创建'xx'文件夹。

## ssh-keygen
生成ssh的公钥和私钥。
私钥不能泄露。
ssh是一个协议名称。

## pwd
查看当前路径。

## git
### git add 'xxx'
把'xxx'文件/文件夹的修改加入缓存区。
### git status
查看当前目录下各文件的状态：修改后/缓存区中会展示出来。
### git commit -m "hahaha"
将当前缓存区的修改同步到电脑内的git仓库，注释为"hahaha"
### git push
将电脑内的git仓库中的修改同步到远程仓库。
### git clone git@github.com:YCorguo/edu_for_dradra.git
将"git@github.com:YCorguo/edu_for_dradra.git"git仓库克隆到本地。如果具有权限，则可以将修改push到远程仓库。

## Esc
退出编辑模式。

## :
### 要用英文的冒号
### w 保存
### q 退出
### q! 强制退出
### set paste 粘贴模式
