
## mac 使用 ntfs （u盘）

```bash
brew install --cask macfuse
brew tap gromgit/homebrew-fuse
brew install ntfs-3g-mac

# 查看u盘式哪个
diskutil list （eg. /dev/disk4s1）

# mkdir ~/Desktop/NTFS_Drive
sudo /usr/local/sbin/mount_ntfs /dev/disk4s1 ~/Desktop/NTFS_Drive

```
