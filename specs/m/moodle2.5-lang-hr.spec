# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename hr
%define packagversion 2.5.0
%define packagedate 201602031855
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname Croatian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-hr
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
* Sun Feb 07 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201602031855-alt1
- repocop cronbuild 20160207. At your service.
- hr.zip build 2016-02-03 18:55 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201601131241-alt1
- repocop cronbuild 20160124. At your service.
- hr.zip build 2016-01-13 12:41 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511270748-alt1
- repocop cronbuild 20151130. At your service.
- hr.zip build 2015-11-27 07:48 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511181452-alt1
- repocop cronbuild 20151123. At your service.
- hr.zip build 2015-11-18 14:52 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510061114-alt1
- repocop cronbuild 20151012. At your service.
- hr.zip build 2015-10-06 11:14 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510051040-alt1
- repocop cronbuild 20151005. At your service.
- hr.zip build 2015-10-05 10:40 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509180733-alt1
- repocop cronbuild 20150921. At your service.
- hr.zip build 2015-09-18 07:33 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508201219-alt1
- repocop cronbuild 20150823. At your service.
- hr.zip build 2015-08-20 12:19 UTC

* Fri Apr 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504020926-alt1
- repocop cronbuild 20150403. At your service.
- hr.zip build 2015-04-02 09:26 UTC

* Fri Oct 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410271523-alt1
- repocop cronbuild 20141031. At your service.
- hr.zip build 2014-10-27 15:23 UTC

* Fri Oct 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409281702-alt1
- repocop cronbuild 20141003. At your service.
- hr.zip build 2014-09-28 17:02 UTC

* Fri Sep 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409212014-alt1
- repocop cronbuild 20140926. At your service.
- hr.zip build 2014-09-21 20:14 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409180534-alt1
- repocop cronbuild 20140919. At your service.
- hr.zip build 2014-09-18 05:34 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405290733-alt1
- repocop cronbuild 20140530. At your service.
- hr.zip build 2014-05-29 07:33 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404102041-alt1
- repocop cronbuild 20140411. At your service.
- hr.zip build 2014-04-10 20:41 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402181207-alt1
- repocop cronbuild 20140221. At your service.
- hr.zip build 2014-02-18 12:07 UTC

* Fri Feb 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402061348-alt1
- repocop cronbuild 20140207. At your service.
- hr.zip build 2014-02-06 13:48 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401231346-alt1
- repocop cronbuild 20140124. At your service.
- hr.zip build 2014-01-23 13:46 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- hr.zip build 2013-12-13 05:46 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311241158-alt1
- repocop cronbuild 20131129. At your service.
- hr.zip build 2013-11-24 11:58 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311180123-alt1
- repocop cronbuild 20131122. At your service.
- hr.zip build 2013-11-18 01:23 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311141307-alt1
- repocop cronbuild 20131115. At your service.
- hr.zip build 2013-11-14 13:07 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310211406-alt1
- repocop cronbuild 20131025. At your service.
- hr.zip build 2013-10-21 14:06 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310150951-alt1
- repocop cronbuild 20131018. At your service.
- hr.zip build 2013-10-15 09:51 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310070909-alt1
- repocop cronbuild 20131011. At your service.
- hr.zip build 2013-10-07 09:09 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310011437-alt1
- repocop cronbuild 20131004. At your service.
- hr.zip build 2013-10-01 14:37 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309231808-alt1
- repocop cronbuild 20130927. At your service.
- hr.zip build 2013-09-23 18:08 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309200541-alt1
- repocop cronbuild 20130920. At your service.
- hr.zip build 2013-09-20 05:41 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309021107-alt1
- repocop cronbuild 20130906. At your service.
- hr.zip build 2013-09-02 11:07 UTC

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308301402-alt1
- repocop cronbuild 20130831. At your service.
- hr.zip build 2013-08-30 14:02 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308140759-alt1
- repocop cronbuild 20130817. At your service.
- hr.zip build 2013-08-14 07:59 UTC

* Sat Aug 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308012119-alt1
- repocop cronbuild 20130803. At your service.
- hr.zip build 2013-08-01 21:19 UTC

* Sat Jul 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307180002-alt1
- repocop cronbuild 20130720. At your service.
- hr.zip build 2013-07-18 00:02 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307121421-alt1
- repocop cronbuild 20130713. At your service.
- hr.zip build 2013-07-12 14:21 UTC

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307011509-alt1
- repocop cronbuild 20130706. At your service.
- hr.zip build 2013-07-01 15:09 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306140511-alt1
- repocop cronbuild 20130615. At your service.
- hr.zip build 2013-06-14 05:11 UTC

* Sat Jun 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306062007-alt1
- repocop cronbuild 20130608. At your service.
- hr.zip build 2013-06-06 20:07 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305292351-alt1
- Rename package to moodle2.5-lang-hr
- hr.zip build 2013-05-29 23:51 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305221013-alt1
- repocop cronbuild 20130524. At your service.
- hr.zip build 2013-05-22 10:13 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305071028-alt1
- repocop cronbuild 20130509. At your service.
- hr.zip build 2013-05-07 10:28 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304121334-alt1
- Rename package to moodle2.4-lang-hr
- hr.zip build 2013-04-12 13:34 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304121334-alt1
- repocop cronbuild 20130417. At your service.
- hr.zip build 2013-04-12 13:34 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303081548-alt1
- repocop cronbuild 20130313. At your service.
- hr.zip build 2013-03-08 15:48 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303011658-alt1
- repocop cronbuild 20130304. At your service.
- hr.zip build 2013-03-01 16:58 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302230150-alt1
- repocop cronbuild 20130225. At your service.
- hr.zip build 2013-02-23 01:50 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212032117-alt1
- repocop cronbuild 20121210. At your service.
- hr.zip build 2012-12-03 21:17 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211301744-alt1
- repocop cronbuild 20121203. At your service.
- hr.zip build 2012-11-30 17:44 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211231510-alt1
- repocop cronbuild 20121126. At your service.
- hr.zip build 2012-11-23 15:10 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211151016-alt1
- repocop cronbuild 20121119. At your service.
- hr.zip build 2012-11-15 10:16 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211112332-alt1
- repocop cronbuild 20121112. At your service.
- hr.zip build 2012-11-11 23:32 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211010700-alt1
- repocop cronbuild 20121105. At your service.
- hr.zip build 2012-11-01 07:00 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210051252-alt1
- repocop cronbuild 20121008. At your service.
- hr.zip build 2012-10-05 12:52 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209040805-alt1
- repocop cronbuild 20120904. At your service.
- hr.zip build 2012-09-04 08:05 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208281112-alt1
- repocop cronbuild 20120828. At your service.
- hr.zip build 2012-08-28 11:12 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206051435-alt1
- repocop cronbuild 20120605. At your service.
- hr.zip build 2012-06-05 14:35 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205251909-alt1
- repocop cronbuild 20120529. At your service.
- hr.zip build 2012-05-25 19:09 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- hr.zip build 2012-05-11 11:00 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205081058-alt1
- repocop cronbuild 20120508. At your service.
- hr.zip build 2012-05-08 10:58 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- hr.zip build 2012-04-27 11:30 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204161455-alt1
- repocop cronbuild 20120417. At your service.
- hr.zip build 2012-04-16 14:55 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201202282059-alt1
- Rename package to moodle2.2-lang-hr
- hr.zip build 2012-02-28 20:59 UTC

* Fri Mar 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202282102-alt1
- repocop cronbuild 20120302. At your service.
- hr.zip build 2012-02-28 21:02 UTC

* Fri Feb 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202231326-alt1
- repocop cronbuild 20120224. At your service.
- hr.zip build 2012-02-23 13:26 UTC

* Fri Feb 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202112139-alt1
- repocop cronbuild 20120217. At your service.
- hr.zip build 2012-02-11 21:39 UTC

* Fri Jan 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201091003-alt1
- repocop cronbuild 20120113. At your service.
- hr.zip build 2012-01-09 10:03 UTC

* Fri Dec 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112161412-alt1
- repocop cronbuild 20111216. At your service.
- hr.zip build 2011-12-16 14:12 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- hr.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111122043-alt1
- Rename package to moodle2.1-lang-hr
- hr.zip build 2011-11-12 20:43

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt6
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- hr.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- hr.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-hr
- hr.zip build 2011-08-11 23:00 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt2
- Fix Summary

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- Test build
- hr_utf8.zip build 2010-05-26
- initial build for ALT Linux Sisyphus
