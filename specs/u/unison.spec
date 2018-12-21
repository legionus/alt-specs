Name: unison
Version: 2.51.2
Release: alt2

Summary: File-synchronization tool

Group: Networking/File transfer
License: GPLv2+
Url: http://www.cis.upenn.edu/~bcpierce/unison
# https://github.com/bcpierce00/unison
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: ocaml >= 4.04 ocaml-lablgtk-devel desktop-file-utils
BuildRequires: texlive-collection-latexrecommended texlive-collection-basic ghostscript-utils

%description
Unison is a file-synchronization tool. It allows two replicas of a
collection of files and directories to be stored on different hosts
(or different disks on the same host), modified separately, and then
brought up to date by propagating the changes in each replica to the
other.

%package gui
Summary: GTK+ version of unison file-synchronization tool
Group: Networking/File transfer
%description gui
Unison is a file-synchronization tool. It allows two replicas of a
collection of files and directories to be stored on different hosts
(or different disks on the same host), modified separately, and then
brought up to date by propagating the changes in each replica to the
other.

%prep
%setup
%patch0 -p1

%build
make -C src UISTYLE=text
mv src/unison src/unison-cli
make -C src UISTYLE=gtk2
make docs

%install
install -pDm0755 src/unison-cli %buildroot%_bindir/unison
install -pDm0755 src/unison %buildroot/%_bindir/unison-gui
install -pDm0644 icons/U.svg %buildroot/%_iconsdir/hicolor/scalable/apps/unison.svg


cat > unison.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=unison-gui
Name=Unison File Synchronizer
Name[ru]=Синхронизация файлов Unison
GenericName=File Synchronizer
GenericName[ru]=Синхронизатор файлов
Comment=Multi-master File synchronization tool
Comment[ru]=Утилита синхронизации файлов с поддержкой нескольких полноправных источников
Terminal=false
Icon=unison
Encoding=UTF-8
StartupNotify=true
EOF

desktop-file-install  \
    --add-category Application \
    --add-category Utility \
    --dir %buildroot%_desktopdir \
    unison.desktop


%files
%doc src/COPYING src/RECENTNEWS src/README
%doc doc/unison-manual.pdf
%_bindir/unison

%files gui
%_bindir/unison-gui
%_iconsdir/hicolor/scalable/apps/unison.svg
%_desktopdir/*.desktop

%changelog
* Wed Oct 31 2018 Anton Farygin <rider@altlinux.ru> 2.51.2-alt2
- added unison-gui package with GTK2 UI (closes: #18455)

* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 2.51.2-alt1
- 2.51.2

* Sat Mar 03 2018 Igor Vlasenko <viy@altlinux.ru> 2.48.4-alt2
- NMU: rebuild with TeXLive instead of TeTeX

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 2.48.4-alt1
- new version

* Tue Jun 25 2013 Anton Farygin <rider@altlinux.ru> 2.45.28-alt1
- new version

* Thu Jul 12 2012 Anton Farygin <rider@altlinux.ru> 2.45.4-alt1
- first build for Sisyphus

