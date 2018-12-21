Name: uftp
Version: 4.9.8
Release: alt1

Summary: A multicast FTP

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL
Group: Networking/File transfer
Url: http://uftp-multicast.sourceforge.net/

Source: http://sourceforge.net/projects/uftp-multicast/files/source-tar/uftp-%version.tar

# Automatically added by buildreq on Thu Jan 31 2013
BuildRequires: libssl-devel

%description
UFTP is a multicast file transfer program, utilizing a protocol based on
Starburst MFTP. It is designed to reliably and efficiently transfer files
to multiple receivers simultaneously, where either the intended receivers
can be specified beforehand, or receivers can join the transfer when it is
initiated. This is useful for distributing large files to a large number of
receivers, and is especially useful for data distribution over a satellite
link (with two way communication), where the inherent delay makes any TCP
based communication terribly inefficient. UFTP has been used in the production
process of The Wall Street Journal to send WSJ pages over satellite to their
remote printing plants.

%package server
Summary: A multicast ftp server
Group: Networking/File transfer

%description server
UFTP is a multicast file transfer program, utilizing a protocol based on
Starburst MFTP. It is designed to reliably and efficiently transfer files
to multiple receivers simultaneously, where either the intended receivers
can be specified beforehand, or receivers can join the transfer when it is
initiated. This is useful for distributing large files to a large number of
receivers, and is especially useful for data distribution over a satellite
link (with two way communication), where the inherent delay makes any TCP
based communication terribly inefficient. UFTP has been used in the production
process of The Wall Street Journal to send WSJ pages over satellite to their
remote printing plants.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std
mkdir -p %buildroot%_sbindir/
mv %buildroot%_bindir/{uftpd,uftpproxyd} %buildroot%_sbindir/

%files
%_bindir/uftp
%_bindir/uftp_keymgt
%_man1dir/uftp.1*
%_man1dir/uftp_keymgt.1*
%doc Changes.txt ReadMe.txt

%files server
%_sbindir/uftpd
%_sbindir/uftpproxyd
%_man1dir/uftpd.1*
%_man1dir/uftpproxyd.1*
%doc ReadMe.txt

%changelog
* Thu Sep 13 2018 Vitaly Lipatov <lav@altlinux.ru> 4.9.8-alt1
- new version 4.9.8 (with rpmrb script)

* Sat Aug 22 2015 Vitaly Lipatov <lav@altlinux.ru> 4.7-alt1
- new version 4.7 (with rpmrb script)

* Thu Jan 31 2013 Vitaly Lipatov <lav@altlinux.ru> 3.7.1-alt1
- new version 3.7.1 (with rpmrb script)

* Thu Jan 31 2013 Vitaly Lipatov <lav@altlinux.ru> 2.6.3-alt1
- initial build for ALT Linux Sisyphus

* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.6.3-2mdv2010.0
+ Revision: 434497
- rebuild

* Thu Sep 18 2008 Olivier Thauvin <nanardon@mandriva.org> 2.6.3-1mdv2009.0
+ Revision: 285637
- 2.6.3

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.6.1-3mdv2009.0
+ Revision: 255050
- rebuild

* Thu Feb 21 2008 Olivier Thauvin <nanardon@mandriva.org> 2.6.1-1mdv2008.1
+ Revision: 173678
- import uftp


