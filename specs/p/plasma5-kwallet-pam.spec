%define rname kwallet-pam

Name: plasma5-%rname
Version: 5.12.7
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 PAM KWallet integration
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-defaults.patch

# Automatically added by buildreq on Thu Aug 27 2015 (-bi)
# optimized out: cmake-modules elfutils libgpg-error libgpg-error-devel libstdc++-devel python-base python3 python3-base ruby ruby-stdlibs
#BuildRequires: cmake gcc-c++ glibc-devel-static libgcrypt-devel libpam-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: cmake gcc-c++ glibc-devel extra-cmake-modules qt5-base-devel libgcrypt-devel libpam-devel

Provides: kf5-kwallet-pam = %EVR
Obsoletes: kf5-kwallet-pam < %EVR

%package -n pam0_kwallet
Summary: KDE4 PAM KWallet integration
Group: System/Base
Requires: socat
%description -n pam0_kwallet
KDE4 PAM KWallet integration

%package -n pam0_kwallet5
Summary: KDE5 PAM KWallet integration
Group: System/Base
Requires: socat
%description -n pam0_kwallet5
KDE5 PAM KWallet integration



%description
%summary.

%prep
%setup -n %rname-%version
%patch1 -p1

mkdir kde4
mv c* C* p* kde4
cp -ar kde4 kde5

%build
pushd kde4
%K5build -DKWALLET4=1 -DCMAKE_INSTALL_LIBDIR=/%_lib
popd
pushd kde5
%K5build -DKWALLET5=1 -DCMAKE_INSTALL_LIBDIR=/%_lib
popd

%install
for d in kde4 kde5; do
pushd $d
%K5install
popd
done

# fix libs path
if [  -d %buildroot/%_libdir/security ] ; then
    mkdir -p %buildroot/%_lib/security
    mv %buildroot/%_libdir/security/* %buildroot/%_lib/security/
fi

# install pam_kwallet_init
mkdir -p %buildroot/%_K5libexecdir
cat >%buildroot/%_K5libexecdir/pam_kwallet_init <<__EOF__
#!/bin/sh
if test -n "\$PAM_KWALLET_LOGIN" ; then
    env | socat STDIN UNIX-CONNECT:\$PAM_KWALLET_LOGIN
fi
__EOF__
chmod 0755 %buildroot/%_K5libexecdir/pam_kwallet_init

cat >%buildroot/%_K5libexecdir/pam_kwallet5_init <<__EOF__
#!/bin/sh
if test -n "\$PAM_KWALLET5_LOGIN" ; then
    env | socat STDIN UNIX-CONNECT:\$PAM_KWALLET5_LOGIN
fi
__EOF__
chmod 0755 %buildroot/%_K5libexecdir/pam_kwallet5_init

# install pam_kwallet_init.desktop
cp -ar %buildroot/%_K5start/pam_kwallet_init.desktop \
    %buildroot/%_K5start/pam_kwallet5_init.desktop
sed -i '/^Exec=/s|/pam_kwallet_init|/pam_kwallet5_init|' \
    %buildroot/%_K5start/pam_kwallet5_init.desktop

%files -n pam0_kwallet
%doc kde4/COPYING.LIB
%_pam_modules_dir/pam_kwallet.so
%_K5libexecdir/pam_kwallet_init
%_K5start/pam_kwallet_init.desktop

%files -n pam0_kwallet5
%doc kde5/COPYING.LIB
%_pam_modules_dir/pam_kwallet5.so
%_K5libexecdir/pam_kwallet5_init
%_K5start/pam_kwallet5_init.desktop

%changelog
* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Fri Sep 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt2%ubt
- fix requires (ALT#35393)

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1%ubt
- new version

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1%ubt
- new version
- security fixes: CVE-2018-10380

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1%ubt
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1%ubt
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2%ubt
- renamed kf5-kwallet-pam -> plasma5-kwallet-pam

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1%ubt
- new version

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1%ubt
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1%ubt
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1%ubt
- new version

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1%ubt
- new version

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1%ubt
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt2
- fix path to KDE4 kwalletd

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- initial build
