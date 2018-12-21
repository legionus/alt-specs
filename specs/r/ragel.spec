# vim: set ft=spec: -*- rpm-spec -*-

Name: ragel
Version: 6.10
Release: alt1.1

Summary: Ragel State Machine Compiler
Group: Development/Other
License: GPLv2
Url: http://www.complang.org/ragel/

Source: %name-%version.tar

# Automatically added by buildreq on Fri Jul 25 2008
BuildRequires: gcc-c++ ghostscript-classic texlive-context texlive-collection-latexrecommended transfig vim-devel

%description
Ragel compiles executable finite state machines from regular
languages. Ragel targets C, C++, Objective-C, D, Java and Ruby.
Ragel state machines can not only recognize byte sequences as
regular expression machines do, but can also execute code at
arbitrary points in the recognition of a regular language. Code
embedding is done using inline operators that do not disrupt the
regular language syntax.

%package -n vim-plugin-%name-syntax
Summary: Vim syntax for Ragel
Group: Editors
PreReq: vim-common

%description -n vim-plugin-%name-syntax
Vim syntax for Ragel.

%prep
%setup

%build
%add_optflags -fpermissive
export CPPFLAGS="%optflags"
%configure --docdir=%_docdir/%name-%version
%make_build
%make_build -C doc

%install
mkdir -p %buildroot{%vim_syntax_dir,%vim_ftdetect_dir}
%makeinstall_std
%makeinstall_std -C doc
cp CREDITS README TODO %buildroot%_docdir/%name-%version

install -p -m644 ragel.vim %buildroot%vim_syntax_dir/
cat <<EOF >%buildroot%vim_ftdetect_dir/ragel.vim
au BufNewFile,BufRead *.rl  setf ragel
EOF

%check
#make -C test check

%files
%doc %_docdir/%name-%version
%_bindir/*
%_man1dir/*

%files -n vim-plugin-%name-syntax
%vim_syntax_dir/ragel.vim
%vim_ftdetect_dir/ragel.vim

%changelog
* Sat Mar 03 2018 Igor Vlasenko <viy@altlinux.ru> 6.10-alt1.1
- NMU: rebuild with TeXLive instead of TeTeX
- note: disabled %%check to rebuild successfully

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.10-alt1
- Updated to stable upstream version 6.10

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.8-alt1
- Version 6.8

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.6-alt1.1
- Fixed build with gcc 4.7

* Thu Apr 15 2010 Alexey I. Froloff <raorn@altlinux.org> 6.6-alt1
- [6.6]

* Fri Jul 25 2008 Sir Raorn <raorn@altlinux.ru> 6.2-alt1
- Built for Sisyphus

