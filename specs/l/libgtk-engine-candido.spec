%define _name candido
%define engine_prefix libgtk-engine

Name: %engine_prefix-%_name
Version: 0.9.1
Release: alt1.1.qa1

Summary: Candido GTK2 engine
Summary(ru_RU.UTF-8):Модуль прорисовки Candido для GTK2
License: GPL
Group: Graphical desktop/GNOME
Url: http://candido.berlios.de/pages/engine.php
Source0: %_name-engine-%version.tar.bz2
Patch0: gtk-engines-candido-0.9.1-alt-glib2.patch

%define gtk_ver 2.10.0
%define gtk_binary_ver 2.10.0
%define engines_dir %_libdir/gtk-2.0/%gtk_binary_ver/engines

BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildRequires: gcc-c++ gcc-g77 libgtk+2-devel

%description
This is Candido GTK+ engine based on Doug Whiteley's rezlooks GTK+ engine.

%description -l ru_RU.UTF-8
Это модуль прорисовки Candido для GTK2, основанный на rezlooks от Doug Whiteley.

%prep
%setup -q -n %_name-engine-%version
%patch -p2

%build
%autoreconf
%configure --enable-animation
%make

%install
%makeinstall

%files
%doc AUTHORS README ChangeLog
%engines_dir/*.so
%exclude %engines_dir/*.la

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1.1.qa1
- NMU: applied repocop patch

* Fri Jul 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.1
- Fixed build

* Wed Dec 06 2006 Vyacheslav Dikonov <slava@altlinux.ru> 0.9.1-alt1
- ALTLinux build
