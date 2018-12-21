%define Name QXmlEdit
Name: qxmledit
Version: 0.9.7.1
Release: alt1
Summary: Simple XML editor and XSD viewer
Group: Editors
License: GPLv2+
URL: https://github.com/lbellonda/%name
Source: %name-%version.tar
#Patch: %%name-%%version-%%release.patch
Provides: %Name = %version-%release

BuildRequires: gcc-c++ libqt4-devel rpm-macros-qt4

%description
%Name is a simple XML editor written in qt4. Its main features are unusual
data visualization modes, nice XML manipulation and presentation. It can split
very big XML files into fragments, and compare XML files. It is one of the few
graphical Open Source XSD viewers.
Main features:
  - Hierarchical customizable view of XML elements.
  - Fast XML hierarchy navigation.
  - Split of big XML files.
  - Search supporting XPath expressions.
  - Base 64 data handling.
  - Custom visualization styles.
  - XML Schema (XSD) viewer.
  - Columnar view.
  - Sessions handling.
  - Graphical XML file view.
  - Map view of a XML document.
  - Split and fragment extraction of big XML files.
  - Visual compare of XML Schema files.
  - Visual compare of XML files.
  - XML Snippets.
  - XSL specialized mode. 


%prep
%setup -q
#patch -p1


%build
%qmake_qt4 "CONFIG+=release staticlib" %Name.pro
%make_build \
	QXMLEDIT_INST_DATA_DIR=%_datadir/%name \
	QXMLEDIT_INST_DIR=%_bindir \
	QXMLEDIT_INST_DOC_DIR=%_docdir/%name-%version \
	QXMLEDIT_INST_LIB_DIR=%_libdir \
	QXMLEDIT_INST_INCLUDE_DIR=%_includedir/%name


%install
%make_install INSTALL_ROOT=%buildroot install
install -m 0644 AUTHORS NEWS README ROADMAP TODO %buildroot%_docdir/%name-%version/

install -pD -m 0644 src/images/icon.png %buildroot%_niconsdir/%name.png
install -pD -m 0644 ./src/images/icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

install -d -m 0755 %buildroot%_desktopdir
mv %buildroot%_datadir/%name/%Name.desktop %buildroot%_desktopdir/%Name.desktop


%files
%doc %_docdir/%name-%version
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_niconsdir/*
%_iconsdir/hicolor/scalable/apps/*
%exclude %_includedir
%exclude %_libdir


%changelog
* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.7.1-alt1
- Update to upstream version 0.9.7-1

* Sun Mar 30 2014 Led <led@altlinux.ru> 0.8.10-alt1
- initial build
