Name: cachefilesd
Version: 0.10.1
Release: alt1.qa2

Summary: caching backend for use with FS-Cache
License: GPL
Group: Networking/Other
Url: http://people.redhat.com/~dhowells/fscache/

Source: %name-%version-%release.tar

%description
CacheFiles is a caching backend that's meant to use as a cache a directory on
an already mounted filesystem of a local type (such as Ext3).

%prep
%setup

%build
make

%install
make install DESTDIR=%buildroot
install -pD -m0755 cachefilesd.initd %buildroot%_initdir/cachefilesd
mkdir -p %buildroot%_cachedir/fscache

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README howto.txt
%config(noreplace) %_sysconfdir/cachefilesd.conf

%_initdir/%name

/sbin/cachefilesd

%_man5dir/*
%_man8dir/*

%dir %attr(700,root,root) %_cachedir/fscache

%changelog
* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1.qa2
- NMU: added URL

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.10.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Nov 16 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt1
- 0.10.1 released

* Thu Jul  2 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt1
- Initial build

