%define plugname ColorSamplerPack
%define plugver  5.0

Name: vim-plugin-%plugname
Version: %plugver
Release: alt3.1

Summary: Large collection of Vim color schemes
Summary(ru_RU.CP1251): ������� ��������� �������� ���� Vim
Group: Editors
License: Distributable
Url: https://www.vim.org/scripts/script.php?script_id=625
BuildArch: noarch

Source: %plugname.zip
Patch0: %name-5.0-alt-disable-default.patch

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel unzip /usr/bin/vim

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%post
%update_vimhelp

%postun
%clean_vimhelp

%description
This package includes all color themes from vim.sf.net (as of August
31th, 2007). It also contains simple menu with all these themes.

To enable the menu define "use_colorsamplerpack_plugin" variable
somewhere in your .vimrc file.

%description -l ru_RU.CP1251
���� ����� �������� ��� �������� ����� � vim.sf.net �� ��������� �� 31
������� 2007 �., � ����� ����, ���������� ������������ ����� ����.

����� �������� ����, ���������� ���������� use_colorsamplerpack_plugin
� ����� ����� .vimrc.


%prep
%setup -c
%patch0 -p1

%build
# included in main Vim distribution
rm colors/{delek,desert}.vim
cat <<EOS | /usr/bin/vim -E -s -X -N -n -i NONE -u NONE -U NONE
edit colors/ps_color.vim
source %%
write!
quit!
EOS

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a * %buildroot%vim_runtime_dir

%files
%vim_colors_dir/*
%vim_plugin_dir/*
%vim_doc_dir/*.txt

%changelog
* Wed Oct 24 2018 Grigory Ustinov <grenka@altlinux.org> 5.0-alt3.1
- Replace %%vim_script_url macro on real url.

* Fri Oct 03 2008 Andrey Rahmatullin <wrar@altlinux.ru> 5.0-alt3
- rebuild with case preserving %%setup

* Sat May 31 2008 Andrey Rahmatullin <wrar@altlinux.ru> 5.0-alt2
- disable menu generation by default (closes: #15471)

* Sat Mar 29 2008 Andrey Rahmatullin <wrar@altlinux.ru> 5.0-alt1
- 5.0

* Sat May 28 2005 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt1
- 4.0

* Thu Sep 2 2004 Andrey Rahmatullin <wrar@altlinux.ru> 3.0-alt1
- new version
- add Packager:
- add Russian summary and description

* Thu Aug 19 2004 Andrey Rahmatullin <wrar@altlinux.ru> 2.0-alt1.1
- fix buildreqs

* Wed Aug 18 2004 Andrey Rahmatullin <wrar@altlinux.ru> 2.0-alt1
- initial build
