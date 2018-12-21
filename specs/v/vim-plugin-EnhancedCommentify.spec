%define plugname EnhancedCommentify
%define plugver  2.3

Name: vim-plugin-%plugname
Version: %plugver
Release: alt1.1

Summary: Vim plugin for easy (un)commenting code lines
Group: Editors
License: BSD
Url: https://www.vim.org/scripts/script.php?script_id=23
BuildArch: noarch

Source: %plugname-%plugver.tar.gz
Patch: %name-2.1-alt-disable-default.patch

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%post
%update_vimhelp

%postun
%clean_vimhelp

%description
This plugin allows quick (un)commenting lines and text blocks in programs,
scripts etc., supporting many file types.

To enable this plugin define "use_enhcomment_plugin" variable somewhere
in your .vimrc file.

%description -l ru_RU.CP1251
���� ������ ��������� ������ �������������� ������ � ����� ����� � ��������
�������, �������� � �.�., ����������� ��������� ����� ������.

����� �������� ���� ������, ���������� ���������� use_enhcomment_plugin �
����� ����� .vimrc.

%prep
%setup -n %plugname-%plugver
%patch -p1

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a {plugin,ftplugin,doc} %buildroot%vim_runtime_dir

%files
%vim_doc_dir/*
%vim_ftplugin_dir/*
%vim_plugin_dir/*

%changelog
* Wed Oct 24 2018 Grigory Ustinov <grenka@altlinux.org> 2.3-alt1.1
- Replace %%vim_script_url macro on real url.

* Sat Mar 29 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.3-alt1
- 2.3

* Mon Sep 27 2004 Andrey Rahmatullin <wrar@altlinux.ru> 2.2-alt1
- new version

* Thu Sep 02 2004 Andrey Rahmatullin <wrar@altlinux.ru> 2.1-alt1.1
- add Packager:
- add Russian description

* Wed Aug 18 2004 Andrey Rahmatullin <wrar@altlinux.ru> 2.1-alt1
- initial build
