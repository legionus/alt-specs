
%define lng ru
%define lngg Russian

Name: kf5-i18n-%lng
Version: 5.12.0
Release: alt1%ubt

Group: Graphical desktop/KDE
Summary: %lngg language support for KDE Workspace
License: GPL
Url: http://www.kde.org/

Requires: kf5-filesystem
BuildArch: noarch

Source0: kf5-l10n-%lng-messages-%version.tar
Source1: kf5-l10n-%lng-docs-%version.tar
Source100: template-main
Source101: template-messages
Patch1: alt-breeze-tooltips.patch

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libdb4-devel qt5-tools-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel

%description
%lngg language support for KDE.


%prep
%setup -T -c -n %name-%version -a0 -a1
for d in *-l10n-* ; do
    simplename=`echo "$d" | sed -e 's|^kf5-l10n-%lng-||' -e 's|-[[:digit:]].*||'`
    mv $d $simplename
done
rm -f messages/*khelpcenter*
rm -rf docs/fundamentals
rm -rf docs/khelpcenter

find docs -type d | \
while read d ; do
    pushd $d
    if [ -f index.docbook ] ; then
	echo "kdoctools_create_handbook(index.docbook INSTALL_DESTINATION \${HTML_INSTALL_DIR}/\${CURRENT_LANG}/ SUBDIR `basename $d` )" >CMakeLists.txt
    elif [ -n "`find ./* -type d`" ] ; then
	ls -1d * | \
	while read docd ; do
	    [ -d "$docd" ] || continue
	    echo "add_subdirectory( $docd )" >>CMakeLists.txt
	done
    else
	echo >CMakeLists.txt
    fi
    popd
done

cat %SOURCE101 >messages/CMakeLists.txt

cat %SOURCE100 >CMakeLists.txt
sed -i 's|@LANGSHORT@|%lng|' CMakeLists.txt
ls -1d * | \
while read d ; do
    [ -d "$d" ] || continue
    echo "add_subdirectory( $d )" >> CMakeLists.txt
done
%patch1 -p1


%files
#%dir %_K5doc/%lng/
#%lang(%lng) %_K5doc/%lng/*
#
#%dir %_K5i18n/%lng/
#
#%dir %_K5i18n/%lng/LC_MESSAGES/
#%lang(%lng) %_K5i18n/%lng/LC_MESSAGES/*.mo

%changelog
* Wed Nov 08 2017 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1%ubt
- don't package translations

* Fri Aug 11 2017 Oleg Solovyov <mcpain@altlinux.org> 5.10.4-alt2%ubt
- add tooltips on window decoration buttons translation

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Tue Apr 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1
- new version

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Wed Oct 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Fri Oct 07 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Fri Jul 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt2
- remove khelpcenter translation

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Wed Feb 03 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt2
- update user switcher translation

* Tue Feb 02 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- initial build
