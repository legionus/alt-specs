%define plugname lh_cpp
%define plugtype ftplugin
%define plugver  20040316

Name: vim-plugin-%plugname-%plugtype
Version: %plugver
Release: alt2.1

Summary: Collection of plugins for editing C/C++ files
Summary(ru_RU.CP1251): ��������� �������� ��� �������������� ���������� �� C/C++

Group: Editors
License: Distributable
Url: https://www.vim.org/scripts/script.php?script_id=336
BuildArch: noarch

Source: lh-cpp.tar.gz
Patch: %name-20040316-alt-disable-default.patch

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%post
%update_vimhelp

%postun
%clean_vimhelp

%description
This package contains several ftplugins addressed at the edition of C
and C++ files. It also includes folding settings for C/C++. 
You should read :help lh-cpp-first-steps if you are using these plugins
for the first time.

To enable these plugins define "use_lh_cpp_ftplugin" variable somewhere
in your .vimrc file. To enable C/C++ folding (very slow) define
"use_lh_cpp_folding".

%description -l ru_RU.CP1251
���� ����� �������� ��������� �������� ��� �������������� �������� ������
�� C/C++, � ����� ��������� �������� ��� C/C++ �� ������ ����������. �����
1-� �������������� ���� �������� ���������� :help lh-cpp-first-steps.

����� �������� ��� �������, ���������� ���������� use_lh_cpp_ftplugin �
����� ����� .vimrc. ����� �������� ������� ��� C/C++ (����� ���������),
���������� ���������� use_lh_cpp_folding.

%prep
%setup -q -n lh-cpp
%patch -p1
%__subst 's,\r,,' syntax/doxygen.vim

%build
%__rm -f ftplugin/c/doc/tags
%__mv ftplugin/c/doc/lh-cpp-readme.txt doc/
%__mv fold/c-fold.vim ftplugin/c_fold.vim

%install
%__mkdir_p %buildroot%vim_runtime_dir
%__cp -a {after,doc,ftplugin,plugin,syntax} %buildroot%vim_runtime_dir
%__rm -rf %buildroot%vim_runtime_dir/{after/template/lie-dans.sh,ftplugin/c/doc}

%files
%doc changelog-cpp after/template/lie-dans.sh ftplugin/c/doc/c.html
%vim_after_plugin_dir/*
%vim_after_dir/template
%vim_doc_dir/*
%vim_ftplugin_dir/*
%vim_plugin_dir/*
%vim_syntax_dir/*

%changelog
* Wed Oct 24 2018 Grigory Ustinov <grenka@altlinux.org> 20040316-alt2.1
- Replace %%vim_script_url macro on real url.

* Thu Sep 02 2004 Andrey Rahmatullin <wrar@altlinux.ru> 20040316-alt1.1
- add Packager:
- add Russian summary and description

* Tue Aug 17 2004 Andrey Rahmatullin <wrar@altlinux.ru> 20040316-alt1
- initial build
