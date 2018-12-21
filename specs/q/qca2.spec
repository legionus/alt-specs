%define libdir_link %_qt4dir/lib

Name: qca2
%define major 2
%define minor 2
%define bugfix 0
Version: %major.%minor.%bugfix
Release: alt0.1%ubt

Group: Networking/Instant messaging
Summary: QCA - Qt Cryptographic Architecture
License: LGPL
Url: https://userbase.kde.org/QCA

Requires: lib%name = %version-%release

Source: qca-%version.tar.bz2
# ALT
Patch10: qca-2.0.3-alt-paths.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake gcc-c++ glibc-devel kde-common-devel ca-certificates
BuildRequires: libgcrypt-devel libnss-devel libqt4-devel libsasl2-devel pkcs11-helper-devel


%package -n lib%name
Summary: QCA - Qt Cryptographic Architecture library
Summary(ru_RU.UTF-8): Файлы, необходимые для разработки приложений с использованием Qt Crytographic Architecture (QCA)
Group: System/Libraries
Requires: ca-certificates

%package -n lib%name-devel
Summary: Header files for developing apps which will use Qt Crytographic Architecture (QCA)
Summary(ru_RU.UTF-8): Файлы, необходимые для разработки приложений с использованием Qt Crytographic Architecture (QCA)
Group: Development/KDE and QT
Requires: libqt4-devel
Requires: lib%name = %version-%release

%description
  This library provides an easy API for the following features: SSL/TLS,
X509, SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Functionality is supplied via plugins.  This is useful for avoiding
dependence on a particular crypto library and makes upgrading easier,
as there is no need to recompile your application when adding or
upgrading a crypto plugin.  Also, by pushing crypto functionality into
plugins, your application is free of legal issues, such as export
regulation.
%description -l ru_RU.UTF-8
  Эта библиотека предоставляет простой API для следующего: SSL/TLS, X509,
SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Функциональность дополняется с помощью плагинов. Это удобно, так как
избегается зависимость на конкретную криптографическую библиотеку и это
делает обновления проще, так как нет необходимости перекомпилировать
использующее QCA приложение при добавлении или обновлении
крипто-плагина. Также, так как функциональность криптографии вынесена на
уровень плагинов, приложение избавляется от возможных ограничений,
накладываемых законом, например, экспортных ограничений.
%description -n lib%name
  This library provides an easy API for the following features: SSL/TLS,
X509, SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Functionality is supplied via plugins.  This is useful for avoiding
dependence on a particular crypto library and makes upgrading easier,
as there is no need to recompile your application when adding or
upgrading a crypto plugin.  Also, by pushing crypto functionality into
plugins, your application is free of legal issues, such as export
regulation.
%description -n lib%name -l ru_RU.UTF-8
  Эта библиотека предоставляет простой API для следующего: SSL/TLS, X509,
SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Функциональность дополняется с помощью плагинов. Это удобно, так как
избегается зависимость на конкретную криптографическую библиотеку и это
делает обновления проще, так как нет необходимости перекомпилировать
использующее QCA приложение при добавлении или обновлении
крипто-плагина. Также, так как функциональность криптографии вынесена на
уровень плагинов, приложение избавляется от возможных ограничений,
накладываемых законом, например, экспортных ограничений.
%description -n lib%name-devel
This package contains the header files needed to develop programs
that use QCA.
%description -n lib%name-devel -l ru_RU.UTF-8
Этот пакет содержит файлы заголовков, необходимые для разработки
приложений, использующих QCA.

%package ossl
Group: System/Libraries
Summary: QCA SSL Plugin
%description ossl
This is a plugin to provide SSL capability to programs that
utilize the Qt Cryptographic Architecture (QCA)
* Hashing - SHA1, SHA0, RIPEMD160, MD2, MD4, MD5
* Hashing - SHA224, SHA256, SHA384 and SHA512 (for openssl 0.9.8)
* Block Ciphers
* Keyed Hash Message Authentication Code (HMAC), using SHA1, MD5, RIPEMD160
* Public keys - RSA, DSA, Diffie-Hellman
* PKCS#12
* SSL/TLS
* CMS (for S/MIME)
%description ossl -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования SSL для
программ, поддерживающих Qt Cryptographic Architecture (QCA)
* Hashing - SHA1, SHA0, RIPEMD160, MD2, MD4, MD5
* Hashing - SHA224, SHA256, SHA384 and SHA512 (for openssl 0.9.8)
* Block Ciphers
* Keyed Hash Message Authentication Code (HMAC), using SHA1, MD5, RIPEMD160
* Public keys - RSA, DSA, Diffie-Hellman
* PKCS#12
* SSL/TLS
* CMS (for S/MIME)

%package cyrus-sasl
Group: System/Libraries
Summary: QCA SASL Plugin
%description cyrus-sasl
This is a plugin to provide SASL capability to programs that
utilize the Qt Cryptographic Architecture (QCA).
%description cyrus-sasl -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования SASL для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%package gnupg
Group: System/Libraries
Summary: QCA GnuPG Plugin
%description gnupg
This is a plugin to provide GnuPG capability to programs that
utilize the Qt Cryptographic Architecture (QCA).
%description gnupg -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования GnuPG для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%package nss
Group: System/Libraries
Summary: QCA NSS Plugin
%description nss
This is a plugin to provide Mozilla NSS capability to programs that
utilize the Qt Cryptographic Architecture (QCA)
* Hashing
%description nss -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования Mozilla NSS для
программ, поддерживающих Qt Cryptographic Architecture (QCA)
* Хеширование

%package gcrypt
Group: System/Libraries
Summary: QCA GCrypt Plugin
%description gcrypt
This plugin provides features based on libgcrypt to programs that
utilize the Qt Cryptographic Architecture (QCA)
* Hashing - SHA1, SHA256, SHA384, SHA512
* Symmetric encryption - AES128
%description gcrypt -l ru_RU.UTF-8
Этот плагин предоставляет функциональность libgcrypt для
программ, поддерживающих Qt Cryptographic Architecture (QCA)
* Хеширование - SHA1, SHA256, SHA384, SHA512
* Симметричное шифрование - AES128

%package pkcs11
Group: System/Libraries
Summary: QCA pkcs11 smartcard integration
%description pkcs11
This plugin supports the following features:
 - Multiple providers
 - Multiple tokens
 - Private key signature and decryption
 - Keystore objects serialization
 - Keystore update notifications
 - Asker integration for token and PIN

%package logger
Group: System/Libraries
Summary: QCA Logger Plugin
%description logger
Provides simple logger writer to programs that
utilize the Qt Cryptographic Architecture (QCA).
%description logger -l ru_RU.UTF-8
Этот плагин предоставляет возможность записи журналов для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%package softstore
Group: System/Libraries
Summary: QCA Logger Plugin
%description softstore
Provides simple persistent certificate store to programs that
utilize the for Qt Cryptographic Architecture (QCA).
%description softstore -l ru_RU.UTF-8
Этот плагин предоставляет хранилище сертификатов для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%prep
%setup -q -n qca-%version
%patch10 -p1


%build
export QTDIR=%_qt4dir
export QC_CERTSTORE_PATH="%_datadir/ca-certificates/ca-bundle.crt"
%Kbuild \
    -DBUILD_TESTS=OFF \
    -DQCA_INSTALL_IN_QT_PREFIX=ON \
    -Dqca_CERTSTORE=%_datadir/ca-certificates/ca-bundle.crt \
    -DQCA_GPG_EXECUTABLE=gpg \
    -DQT4_BUILD=ON \
    #

%install
%Kinstall

mkdir -p %buildroot/%_bindir
ls -1d %buildroot/%_qt4dir/bin/* 2>/dev/null | while read f ; do
    [ -f "$f" ] || continue
    fname=`basename $f`
    mv $f %buildroot/%_bindir/${fname}-qt4
    ln -s `relative %_bindir/${fname}-qt4 %_qt4dir/bin/$fname-qt4` %buildroot/%_qt4dir/bin/$fname
done

[ -d %buildroot/%libdir_link/pkgconfig ] \
    && mv %buildroot/%libdir_link/pkgconfig %buildroot/%_libdir

mkdir -p %buildroot/%_datadir/qt4
[ -d %buildroot/%prefix/mkspecs ] \
    && mv %buildroot/%prefix/mkspecs %buildroot/%_datadir/qt4

mkdir %buildroot/%libdir_link
pushd %buildroot/%_libdir
for f in lib*.so*
do
    ln -s `relative %buildroot/%_libdir/$f %buildroot/%libdir_link/$f` %buildroot/%libdir_link/$f
done
popd


%files
%_bindir/*
%_qt4dir/bin/*
#%_man1dir/*

%files -n lib%name
%_libdir/lib*.so.*
%doc README INSTALL TODO

%files logger
%_qt4dir/plugins/crypto/libqca-logger.so
%files softstore
%_qt4dir/plugins/crypto/libqca-softstore.so
%files ossl
%_qt4dir/plugins/crypto/libqca-ossl.so
%files cyrus-sasl
%_qt4dir/plugins/crypto/libqca-cyrus-sasl.so
%files gnupg
%_qt4dir/plugins/crypto/libqca-gnupg.so
%files gcrypt
%_qt4dir/plugins/crypto/libqca-gcrypt.so
%files nss
%_qt4dir/plugins/crypto/libqca-nss.so
%files pkcs11
%_qt4dir/plugins/crypto/libqca-pkcs11.so

%files -n lib%name-devel
%_libdir/lib*.so
%libdir_link/lib*.so
%libdir_link/lib*.so.*
%_pkgconfigdir/qca2.pc
%_libdir/cmake/Qca/
%_datadir/qt4/mkspecs/features/crypto.prf
%_includedir/qt4/QtCrypto

%changelog
* Wed Aug 29 2018 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt0.1%ubt
- 2.2.0 snapshot

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2
- NMU: added URL

* Tue Oct 06 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version

* Thu Jun 25 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.0.3-alt2
- rebuild with new libgcrypt

* Wed May 27 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.0.3-alt1
- new version

* Wed Oct 30 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt5
- rebuilt with new libsasl2

* Wed Oct 03 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt4
- fix against gcc-4.7

* Tue Jul 24 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt2.M60P.1
- built for M60P

* Tue Jul 24 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt3
- built pkcs11 plugin

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt2
- fix build requires

* Fri Feb 25 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt1
- new version
- sources taken from kde svn

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt2
- rebuilt with new ssl

* Fri Jun 26 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt0.M50.1
- build for M50

* Fri Jun 26 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- new version

* Tue Mar 31 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1.M50.1
- built for M50

* Tue Mar 31 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt2
- fix to work QT_CONFIG += crypto

* Wed Aug 06 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.1-alt1
- new version

* Wed Mar 19 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.0-alt2
- fix pkgconfig file

* Tue Mar 18 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.0-alt1
- initial specfile
