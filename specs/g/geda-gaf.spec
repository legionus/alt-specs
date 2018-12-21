# As from 1.5, all the submodules of geda-gaf are packaged by upstream into one
# big tarball. This requires a new fedora package review and obsoleting the old.
# geda-* packages fedora was providing, which explains the use of Epoch

%define major 1.9

Name: geda-gaf
Version: %major.2
Release: alt1
Epoch: 2

Summary: Design Automation toolkit for electronic design

License: GPLv2
Group: Video
Url: http://www.geda-project.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.geda-project.org/geda-gaf/unstable/v%major/%version/geda-gaf-%version.tar

Patch: %name.patch

# Automatically added by buildreq on Tue Mar 30 2010
BuildRequires: desktop-file-utils flex git-core glibc-devel groff-base guile22-devel libgtk+2-devel makeinfo

%description
The GPL Electronic Design Automation (gEDA) project has produced and
continues working on a full GPL'd suite and toolkit of Electronic
Design Automation tools. These tools are used for electrical circuit
design, schematic capture, simulation, prototyping, and production.

Currently, the gEDA project offers a mature suite of free software
applications for electronics design, including schematic capture,
attribute management, bill of materials (BOM) generation, netlisting
into over 20 netlist formats, analog and digital simulation, and
printed circuit board (PCB) layout.

%package -n libgeda
Summary: Libraries for the gEDA project
Group: System/Libraries

%description -n libgeda
This package contains libgeda, the library needed by gEDA applications.

%package -n libgeda-devel
Summary: Development files for the libgeda library
Group: Development/C
Requires: libgeda = %epoch:%version-%release

%description -n  libgeda-devel
Development files for libgeda library

%package -n geda-symbols
Summary: Electronic symbols for gEDA
Group: Video
BuildArch: noarch

%description -n geda-symbols
This package contains a bunch of symbols of electronic devices
used by gschem, the gEDA project schematic editor.

%package -n geda-docs
Summary: Documentation and Examples for gEDA
Group: Video
BuildArch: noarch
Requires: geda-symbols
Provides: geda-examples = %epoch:%version-%release
Obsoletes: geda-examples

%description -n geda-docs
This package contains documentation and examples for the gEDA project.

%package -n geda-gattrib
Summary: Attribute editor for gEDA
Group: Video
Requires: geda-symbols

%description -n geda-gattrib
Gattrib is gEDA's attribute editor. It reads a set of gschem .sch files
(schematic files), and creates a spreadsheet showing all components in
rows, with the associated component attributes listed in the columns.
It allows the user to add, modify, or delete component attributes outside
of gschem, and then save the .sch files back out. When it is completed,
it will allow the user to edit attributes attached to components, nets,
and pins. (Currently, only component attribute editing is implemented;
pin attributes are displayed only, and net attributes are TBD.)

%package -n geda-gnetlist
Summary: Netlister for the gEDA project
Group: Video
Requires: geda-symbols

%description -n  geda-gnetlist
Gnetlist generates netlists from schematics drawn with gschem
(the gEDA schematic editor). Possible output formats are:
native, tango, spice, allegro, PCB, verilog and others.

%package -n  geda-gschem
Summary: Electronics schematics editor
Group: Video
Requires: libgeda = %epoch:%version-%release
Requires: geda-symbols
Requires: geda-docs

%description -n geda-gschem
Gschem is an electronics schematic editor. It is part of the gEDA project.

%package -n geda-gsymcheck
Summary: Symbol checker for electronics schematics editor
Group: Video
Requires: geda-symbols

%description -n geda-gsymcheck
Gsymcheck is a utility to check symbols for gschem.
It is part of the gEDA project.

%package -n geda-utils
Summary: Several utilities for the gEDA project
Group: Video
Requires: geda-symbols

AutoReq: yes,noperl

%description -n geda-utils
Several utilities for the gEDA project.

%prep
%setup
%patch -p2
%__subst "s|guile-2.0|guile-2.2|" m4/geda-guile.m4

%build
%autoreconf
%configure
# fix rpath
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
# remove direct glib includes
find -name *.c | xargs %__subst "s|#include <glib/g[mt].*||g"
%make_build

%install
%makeinstall_std
%find_lang libgeda45
%find_lang geda-gaf
%find_lang geda-gschem
%find_lang geda-gattrib
%find_lang geda-gnetlist
%find_lang geda-gsymcheck

# Fixing rpaths
%__subst 's|"/lib /usr/lib|"/%_lib %_libdir|' configure

# remove unwanted files
#rm -f %buildroot%_infodir/dir
rm -f %buildroot%_desktopdir/mimeinfo.cache
rm -rf %buildroot%_docdir/%name/readmes/
rm -rf %buildroot%_docdir/%name/man/
rm -f %buildroot/%_datadir/mime/{XMLnamespaces,aliases,generic-icons,globs}
rm -f %buildroot/%_datadir/mime/{globs2,icons,magic,mime.cache,subclasses,treemagic,types}
rm -f %buildroot/%_datadir/mime/version

%files
%doc ABOUT-NLS AUTHORS ChangeLog COPYING README NEWS

%files -n libgeda -f libgeda45.lang
%doc libgeda/{HACKING,ChangeLog*,BUGS,TODO}
%dir %_datadir/gEDA/
%dir %_datadir/gEDA/scheme
%_libdir/libgeda.so.*
%_libdir/libgedacairo.so.*
#_datadir/gEDA/prolog.ps
%_datadir/gEDA/scheme/geda.scm
%_datadir/gEDA/system-gafrc
%_datadir/mime/packages/libgeda.xml

%files -n libgeda-devel
%_includedir/libgeda/
%_includedir/libgedacairo/
%_libdir/libgeda.so
%_libdir/libgedacairo.so
%_pkgconfigdir/libgeda.pc
%_pkgconfigdir/libgedacairo.pc

%files -n geda-symbols
%doc symbols/{AUTHORS,ChangeLog*,README,TODO}
%_datadir/gEDA/sym/
%dir %_datadir/gEDA/gafrc.d/
%_datadir/gEDA/gafrc.d/geda-clib.scm
%_datadir/mime/application/x-geda-symbol.xml
%_iconsdir/hicolor/*/mimetypes/application-x-geda-symbol.*

%files -n geda-docs
%dir %_docdir/%name/
#%doc %_docdir/%name/man/
%doc %_docdir/%name/wiki/
%doc %_docdir/%name/examples/
%doc %_docdir/%name/gedadocs.html
%doc %_docdir/%name/nc.pdf

%files -n geda-gattrib -f geda-gattrib.lang
%doc gattrib/design/{gEDA_Structures_updated.png,ProgramArchitecture.gnumeric}
%doc gattrib/{BUGS,ChangeLog*,NOTES,README,ToDos}
%_bindir/gattrib
%_datadir/gEDA/system-gattribrc
%_datadir/gEDA/gattrib-menus.xml
%_datadir/gEDA/scheme/auto-place-attribs.scm
%_desktopdir/geda-gattrib.desktop
%_iconsdir/hicolor/*/apps/geda-gattrib.*
%_man1dir/gattrib.1.*

%files -n geda-gnetlist -f geda-gnetlist.lang
%doc gnetlist/{BUGS,ChangeLog*,TODO}
#%doc %_docdir/%name/gnetlist
%_bindir/gnetlist
#%_bindir/mk_verilog_syms
#%_bindir/sch2eaglepos.sh
#_bindir/sw2asc
%_datadir/gEDA/scheme/gnet*.scm
%_datadir/gEDA/scheme/auto-place-netname.scm
%_datadir/gEDA/scheme/gnetlist/
%_datadir/gEDA/system-gnetlistrc
%_man1dir/gnetlist.*

%files -n geda-gschem -f geda-gschem.lang
%doc gschem/{BUGS,ChangeLog*,TODO}
%_bindir/gschem
#%_bindir/gschemdoc
%_datadir/gEDA/gschem-colormap-bw
%_datadir/gEDA/icons/
%_datadir/gEDA/scheme/auto-refdes.scm
%_datadir/gEDA/scheme/spice-common.scm
%_datadir/gEDA/scheme/default-attrib-positions.scm
%_datadir/gEDA/scheme/geda-deprecated-config.scm
%_datadir/gEDA/scheme/partslist-common.scm
%_datadir/gEDA/scheme/image.scm
%_datadir/gEDA/scheme/pcb.scm
%_datadir/gEDA/scheme/print.scm
%_datadir/gEDA/scheme/auto-uref.scm
%_datadir/gEDA/scheme/generate_netlist.scm
%_datadir/gEDA/scheme/gschem.scm
%_datadir/gEDA/scheme/list-keys.scm
%_datadir/gEDA/scheme/print-NB-attribs.scm
%_datadir/gEDA/scheme/gschem/
%_datadir/gEDA/scheme/geda/
%_datadir/gEDA/bitmap/gschem-*
%_datadir/gEDA/system-gschemrc
%_datadir/gEDA/gschem-gtkrc
%_datadir/gEDA/gschem-colormap-darkbg
%_datadir/gEDA/gschem-colormap-lightbg
%_datadir/gEDA/print-colormap-darkbg
%_datadir/gEDA/print-colormap-lightbg
%_datadir/gEDA/scheme/color-map.scm
%_datadir/mime/application/x-geda-schematic.xml
%_desktopdir/geda-gschem.desktop
%_man1dir/gschem.*
%_infodir/geda-scheme.*
%_iconsdir/hicolor/*/apps/geda-gschem.*
%_iconsdir/hicolor/*/mimetypes/application-x-geda-schematic.*

%files -n geda-gsymcheck -f geda-gsymcheck.lang
%doc gsymcheck/{BUGS,ChangeLog*,TODO}
#%doc %_docdir/%name/gsymcheck
%_bindir/gsymcheck
%_datadir/gEDA/system-gsymcheckrc
%_man1dir/gsymcheck.*

%files -n geda-utils -f geda-gaf.lang
%doc utils/{ChangeLog*,README,AUTHORS}
#%doc %_docdir/%name/utils
#%doc %_docdir/%name/readmes/
%_bindir/gaf
%_bindir/garchive
%_bindir/schdiff
%_bindir/grenum
#_bindir/gmk_sym
#_bindir/smash_megafile
#_bindir/convert_sym
#_bindir/sarlacc_schem
#_bindir/sarlacc_sym
%_bindir/gsymfix
%_bindir/pcb_backannotate
%_bindir/gschlas
#_bindir/olib
%_bindir/refdes_renum
%_bindir/gsch2pcb
#_bindir/pads_backannotate
%_bindir/tragesym
#%_bindir/gsymupdate
%_bindir/gxyrs
#%_bindir/gnet_hier_verilog.sh
%_datadir/gEDA/system-gschlasrc
%_datadir/gEDA/perl/lib/gxyrs.pm
%_datadir/mime/application/x-geda-gsch2pcb-project.xml
%_iconsdir/hicolor/*/mimetypes/application-x-geda-gsch2pcb-project.*
%_man1dir/gaf.1.*
%_man1dir/grenum.1.*
%_man1dir/gsymfix.1.*
%_man1dir/garchive.1.*
#_man1dir/convert_sym.1.*
#_man1dir/gmk_sym.1.*
%_man1dir/gsch2pcb.1.*
%_man1dir/gschlas.1.*
%_man1dir/gxyrs.1.*
#_man1dir/olib.1.*
#_man1dir/pads_backannotate.1.*
%_man1dir/pcb_backannotate.1.*
%_man1dir/refdes_renum.1.*
#_man1dir/sarlacc_schem.1.*
#_man1dir/sarlacc_sym.1.*
%_man1dir/schdiff.1.*
#_man1dir/smash_megafile.1.*
#_man1dir/sw2asc.1.*
%_man1dir/tragesym.1.*

%changelog
* Mon Jun 25 2018 Vitaly Lipatov <lav@altlinux.ru> 2:1.9.2-alt1
- new version (1.9.2) with rpmgs script

* Thu Dec 11 2014 Vitaly Lipatov <lav@altlinux.ru> 2:1.9.1-alt1
- new version 1.9.1 (with rpmrb script) (ALT bug #30536)

* Thu Sep 05 2013 Vitaly Lipatov <lav@altlinux.ru> 2:1.6.2-alt1
- new version 1.6.2 (with rpmrb script)

* Sat May 05 2012 Vitaly Lipatov <lav@altlinux.ru> 2:1.6.1-alt2
- fix direct glib headers using

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:1.6.1-alt1.2
- Removed bad RPATH

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2:1.6.1-alt1.1
- Rebuild with Python-2.7

* Tue Mar 16 2010 Vitaly Lipatov <lav@altlinux.ru> 2:1.6.1-alt1
- build new version from one tarball (thanks, Fedora)

* Mon Apr 27 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.2-alt2
- update buildreq

* Fri Dec 26 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.2-alt1
- new version (1.4.2)
- remove post/postun sections

* Sun Feb 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.0-alt1
- new version (1.4.0)
- update buildreq

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.2.1-alt1
- new version (1.2.1)
- cleanup spec

* Tue Sep 11 2007 Vitaly Lipatov <lav@altlinux.ru> 1:1.2.0-alt1
- new version (1.2.0)
- use desktop menu

* Fri Jun 08 2007 Vitaly Lipatov <lav@altlinux.ru> 20070526-alt1
- new version (20070526)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 20070216-alt1
- new version (20070216)
- update buildreq, build with guile18, without libstroke

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 20060906-alt0.1
- new version (20060906)
- remove info files

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 20060123-alt0.1
- new version (20060123)

* Wed Sep 14 2005 Vitaly Lipatov <lav@altlinux.ru> 20050820-alt0.1
- new version

* Mon Feb 14 2005 Vitaly Lipatov <lav@altlinux.ru> 20041228-alt0.2
- add menu entry

* Sun Feb 06 2005 Vitaly Lipatov <lav@altlinux.ru> 20041228-alt0.1
- new version

* Tue Dec 14 2004 Vitaly Lipatov <lav@altlinux.ru> 20041214-alt0.1
- first build for ALT Linus Sisyphus
- rename g_key* functions to geda_key*

* Fri Aug 13 2004 Andy Shevchenko <andriy@asplinux.ru>
- update to version 20040111

* Thu Oct 09 2003 Andy Shevchenko <andriy@asplinux.ru>
- update to version 20030901

* Thu Jun 05 2003 Andy Shevchenko <andriy@asplinux.ru>
- update to new version

* Fri Mar 14 2003 Andy Shevchenko <andriy@asplinux.ru>
- update to new version
- rebuild for 8.1

* Sat Nov 30 2002 Pavel Gashev <pax@asplinux.ru>
- buildrequires geda-symbols

* Wed May 8 2002 Andy Shevchenko <andriy@asplinux.ru>
- update to version 20020414
- write build requirements

* Tue Feb 26 2002 Andy Shevchenko <andy@smile.org.ua>
- build rpm

