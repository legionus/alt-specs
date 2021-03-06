# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename hu
%define packagversion 2.5.0
%define packagedate 201603080731
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname Hungarian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-hu
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.5
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.5
Provides: %moodle_name-%packagetype-%packagename-version = %packagedate
Provides: %moodle_name-%packagetype-%packagename = %version-%release
Provides: %moodle_name-%packagetype-%oldpackagename = %version-%release
Conflicts: %moodle_name-%packagetype-%packagename < %version
Conflicts: %moodle_name-%packagetype-%oldpackagename < %version

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-moodle
BuildPreReq: rpm-build-webserver-common
BuildPreReq: rpm-build-licenses

%description
%summary

%prep
%setup

%build

%install
mkdir -p  %buildroot%moodle_langdir/
cp -rp * %buildroot%moodle_langdir/

%files
%moodle_langdir/*

%changelog
* Mon Mar 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201603080731-alt1
- repocop cronbuild 20160321. At your service.
- hu.zip build 2016-03-08 07:31 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511090729-alt1
- repocop cronbuild 20151109. At your service.
- hu.zip build 2015-11-09 07:29 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510200938-alt1
- repocop cronbuild 20151026. At your service.
- hu.zip build 2015-10-20 09:38 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510160847-alt1
- repocop cronbuild 20151019. At your service.
- hu.zip build 2015-10-16 08:47 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510020717-alt1
- repocop cronbuild 20151005. At your service.
- hu.zip build 2015-10-02 07:17 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509150928-alt1
- repocop cronbuild 20150921. At your service.
- hu.zip build 2015-09-15 09:28 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505040725-alt1
- repocop cronbuild 20150508. At your service.
- hu.zip build 2015-05-04 07:25 UTC

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412110619-alt1
- repocop cronbuild 20141212. At your service.
- hu.zip build 2014-12-11 06:19 UTC

* Fri Nov 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411170752-alt1
- repocop cronbuild 20141121. At your service.
- hu.zip build 2014-11-17 07:52 UTC

* Fri Oct 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410130805-alt1
- repocop cronbuild 20141017. At your service.
- hu.zip build 2014-10-13 08:05 UTC

* Fri Sep 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409240608-alt1
- repocop cronbuild 20140926. At your service.
- hu.zip build 2014-09-24 06:08 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409050516-alt1
- repocop cronbuild 20140919. At your service.
- hu.zip build 2014-09-05 05:16 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406300946-alt1
- repocop cronbuild 20140705. At your service.
- hu.zip build 2014-06-30 09:46 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406112142-alt1
- repocop cronbuild 20140613. At your service.
- hu.zip build 2014-06-11 21:42 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405290657-alt1
- repocop cronbuild 20140530. At your service.
- hu.zip build 2014-05-29 06:57 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405090752-alt1
- repocop cronbuild 20140509. At your service.
- hu.zip build 2014-05-09 07:52 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404160932-alt1
- repocop cronbuild 20140418. At your service.
- hu.zip build 2014-04-16 09:32 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404030940-alt1
- repocop cronbuild 20140404. At your service.
- hu.zip build 2014-04-03 09:40 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403140622-alt1
- repocop cronbuild 20140314. At your service.
- hu.zip build 2014-03-14 06:22 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402270817-alt1
- repocop cronbuild 20140228. At your service.
- hu.zip build 2014-02-27 08:17 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402170731-alt1
- repocop cronbuild 20140221. At your service.
- hu.zip build 2014-02-17 07:31 UTC

* Fri Jan 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401300731-alt1
- repocop cronbuild 20140131. At your service.
- hu.zip build 2014-01-30 07:31 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401231346-alt1
- repocop cronbuild 20140124. At your service.
- hu.zip build 2014-01-23 13:46 UTC

* Fri Dec 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312201640-alt1
- repocop cronbuild 20131227. At your service.
- hu.zip build 2013-12-20 16:40 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- hu.zip build 2013-12-13 05:46 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312031049-alt1
- repocop cronbuild 20131206. At your service.
- hu.zip build 2013-12-03 10:49 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311260841-alt1
- repocop cronbuild 20131129. At your service.
- hu.zip build 2013-11-26 08:41 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311210957-alt1
- repocop cronbuild 20131122. At your service.
- hu.zip build 2013-11-21 09:57 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311121040-alt1
- repocop cronbuild 20131115. At your service.
- hu.zip build 2013-11-12 10:40 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311050715-alt1
- repocop cronbuild 20131108. At your service.
- hu.zip build 2013-11-05 07:15 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310281429-alt1
- repocop cronbuild 20131101. At your service.
- hu.zip build 2013-10-28 14:29 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310150624-alt1
- repocop cronbuild 20131018. At your service.
- hu.zip build 2013-10-15 06:24 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310070954-alt1
- repocop cronbuild 20131011. At your service.
- hu.zip build 2013-10-07 09:54 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310020920-alt1
- repocop cronbuild 20131004. At your service.
- hu.zip build 2013-10-02 09:20 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309250815-alt1
- repocop cronbuild 20130927. At your service.
- hu.zip build 2013-09-25 08:15 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309130853-alt1
- repocop cronbuild 20130913. At your service.
- hu.zip build 2013-09-13 08:53 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309021107-alt1
- repocop cronbuild 20130906. At your service.
- hu.zip build 2013-09-02 11:07 UTC

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308301402-alt1
- repocop cronbuild 20130831. At your service.
- hu.zip build 2013-08-30 14:02 UTC

* Sat Aug 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308230826-alt1
- repocop cronbuild 20130824. At your service.
- hu.zip build 2013-08-23 08:26 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308130937-alt1
- repocop cronbuild 20130817. At your service.
- hu.zip build 2013-08-13 09:37 UTC

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308090713-alt1
- repocop cronbuild 20130810. At your service.
- hu.zip build 2013-08-09 07:13 UTC

* Sat Aug 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308021856-alt1
- repocop cronbuild 20130803. At your service.
- hu.zip build 2013-08-02 18:56 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307260951-alt1
- repocop cronbuild 20130727. At your service.
- hu.zip build 2013-07-26 09:51 UTC

* Sat Jul 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307181356-alt1
- repocop cronbuild 20130720. At your service.
- hu.zip build 2013-07-18 13:56 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307090947-alt1
- repocop cronbuild 20130713. At your service.
- hu.zip build 2013-07-09 09:47 UTC

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307050922-alt1
- repocop cronbuild 20130706. At your service.
- hu.zip build 2013-07-05 09:22 UTC

* Sat Jun 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306240656-alt1
- repocop cronbuild 20130629. At your service.
- hu.zip build 2013-06-24 06:56 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306140511-alt1
- repocop cronbuild 20130615. At your service.
- hu.zip build 2013-06-14 05:11 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305292351-alt1
- Rename package to moodle2.5-lang-hu
- hu.zip build 2013-05-29 23:51 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305222323-alt1
- repocop cronbuild 20130524. At your service.
- hu.zip build 2013-05-22 23:23 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304100856-alt1
- Rename package to moodle2.4-lang-hu
- hu.zip build 2013-04-10 08:56 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211010700-alt1
- repocop cronbuild 20121105. At your service.
- hu.zip build 2012-11-01 07:00 UTC

* Wed Sep 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209070909-alt1
- repocop cronbuild 20120912. At your service.
- hu.zip build 2012-09-07 09:09 UTC

* Wed Sep 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311030-alt1
- repocop cronbuild 20120905. At your service.
- hu.zip build 2012-08-31 10:30 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207180805-alt1
- repocop cronbuild 20120724. At your service.
- hu.zip build 2012-07-18 08:05 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207090940-alt1
- repocop cronbuild 20120710. At your service.
- hu.zip build 2012-07-09 09:40 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207030930-alt1
- repocop cronbuild 20120703. At your service.
- hu.zip build 2012-07-03 09:30 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206200948-alt1
- repocop cronbuild 20120626. At your service.
- hu.zip build 2012-06-20 09:48 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206190927-alt1
- repocop cronbuild 20120619. At your service.
- hu.zip build 2012-06-19 09:27 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206120849-alt1
- repocop cronbuild 20120612. At your service.
- hu.zip build 2012-06-12 08:49 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205300720-alt1
- repocop cronbuild 20120605. At your service.
- hu.zip build 2012-05-30 07:20 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205250834-alt1
- repocop cronbuild 20120529. At your service.
- hu.zip build 2012-05-25 08:34 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205170750-alt1
- repocop cronbuild 20120522. At your service.
- hu.zip build 2012-05-17 07:50 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- hu.zip build 2012-05-11 11:00 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205080948-alt1
- repocop cronbuild 20120508. At your service.
- hu.zip build 2012-05-08 09:48 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- hu.zip build 2012-04-27 11:30 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204020909-alt1
- repocop cronbuild 20120403. At your service.
- hu.zip build 2012-04-02 09:09 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203230940-alt1
- repocop cronbuild 20120327. At your service.
- hu.zip build 2012-03-23 09:40 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203191059-alt1
- Rename package to moodle2.2-lang-hu
- hu.zip build 2012-03-19 10:59 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203191038-alt1
- repocop cronbuild 20120320. At your service.
- hu.zip build 2012-03-19 10:38 UTC

* Tue Mar 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120306. At your service.
- hu.zip build 2012-03-01 11:00 UTC

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201260937-alt1
- repocop cronbuild 20120131. At your service.
- hu.zip build 2012-01-26 09:37 UTC

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201160835-alt1
- repocop cronbuild 20120117. At your service.
- hu.zip build 2012-01-16 08:35 UTC

* Tue Dec 27 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112270855-alt1
- repocop cronbuild 20111227. At your service.
- hu.zip build 2011-12-27 08:55 UTC

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112121017-alt1
- repocop cronbuild 20111213. At your service.
- hu.zip build 2011-12-12 10:17 UTC

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112050908-alt1
- repocop cronbuild 20111206. At your service.
- hu.zip build 2011-12-05 09:08 UTC

* Mon Nov 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111281057-alt1
- repocop cronbuild 20111128. At your service.
- hu.zip build 2011-11-28 10:57 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111220749-alt1
- Rename package to moodle2.1-lang-hu
- hu.zip build 2011-11-22 07:49

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111220640-alt2
- Fix requires

* Wed Nov 23 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111220640-alt1
- repocop cronbuild 20111123. At your service.
- hu.zip build 2011-11-22 06:40 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031015-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031015-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111031015-alt1
- repocop cronbuild 20111105. At your service.
- hu.zip build 2011-11-03 10:15 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210626-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210626-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210626-alt1
- hu.zip build 2011-10-21 06:26 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109261505-alt1
- hu.zip build 2011-09-26 15:05 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- hu.zip build 2011-09-21 15:30 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109120629-alt1
- hu.zip build 2011-09-12 06:29 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108290825-alt1
- hu.zip build 2011-08-29 08:25 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- hu.zip build 2011-08-16 13:07 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-hu
- hu.zip build 2011-08-11 23:00 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.19.10.20100526-alt1
- hu_utf8.zip build 2010-05-26
- initial build for ALT Linux Sisyphus
