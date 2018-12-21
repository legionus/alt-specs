%define cid            langpack-uk@firefox.mozilla.org
%define cid_dir        %firefox_noarch_extensionsdir/%cid

%define cid_dict       uk@dictionaries.addons.mozilla.org
%define cid_dict_dir   %firefox_noarch_extensionsdir/%cid_dict

Name: firefox-uk
Version:	63.0.1
Release: alt1

Summary: Ukrainian (UA) Language Pack for Firefox
License: %gpl2plus
Group: Networking/WWW

URL: http://www.mozilla.org.ua
Source: uk.xpi

Packager: Alexey Gladkov <legion@altlinux.ru>

Requires: hunspell-uk
BuildArch: noarch

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires: unzip

%description
The Mozilla Firefox Ukrainian translation.

%prep
%setup -c -n %name-%version/%cid

%install
cd ..

mkdir -p -- \
	%buildroot/%cid_dir \
	%buildroot/%cid_dict_dir/dictionaries

# Install translation
cp -r -- %cid/* %buildroot/%cid_dir

# Install dictionary
cat > %buildroot/%cid_dict_dir/install.rdf <<-EOF
	<?xml version="1.0"?>
	<RDF xmlns="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	     xmlns:em="http://www.mozilla.org/2004/em-rdf#">
	  <Description about="urn:mozilla:install-manifest"
	               em:id="%cid_dict"
	               em:name="Ukrainian (UA) Dictionary"
	               em:version="%version"
	               em:type="64"
	               em:unpack="true"
	               em:creator="Mozilla Russia">
	    <em:targetApplication>
	      <Description>
	        <em:id>{ec8030f7-c20a-464f-9b0e-13a3a9e97384}</em:id>
	        <em:minVersion>%version</em:minVersion>
	        <em:maxVersion>%version.*</em:maxVersion>
	      </Description>
	    </em:targetApplication>
	  </Description>
	</RDF>
EOF
ln -s %_datadir/myspell/uk_UA.aff %buildroot/%cid_dict_dir/dictionaries/uk.aff
ln -s %_datadir/myspell/uk_UA.dic %buildroot/%cid_dict_dir/dictionaries/uk.dic


%files
%cid_dir
%cid_dict_dir

%changelog
* Tue Nov 13 2018 Alexey Gladkov <legion@altlinux.ru> 63.0.1-alt1
- New version (63.0.1).

* Fri Oct 05 2018 Alexey Gladkov <legion@altlinux.ru> 62.0.3-alt1
- New version (62.0.3).

* Wed Jul 04 2018 Alexey Gladkov <legion@altlinux.ru> 61.0-alt1
- New version (61.0).

* Wed May 23 2018 Alexey Gladkov <legion@altlinux.ru> 60.0.1-alt1
- New version (60.0.1).

* Tue Mar 27 2018 Alexey Gladkov <legion@altlinux.ru> 59.0.2-alt1
- New version (59.0.2).

* Mon Feb 12 2018 Alexey Gladkov <legion@altlinux.ru> 58.0.2-alt1
- New version (58.0.2).

* Mon Dec 04 2017 Alexey Gladkov <legion@altlinux.ru> 57.0.1-alt1
- New version (57.0.1).

* Fri Oct 13 2017 Alexey Gladkov <legion@altlinux.ru> 56.0-alt1
- New version (56.0).

* Mon Aug 14 2017 Alexey Gladkov <legion@altlinux.ru> 55.0.1-alt1
- New version (55.0.1).

* Thu Jul 13 2017 Alexey Gladkov <legion@altlinux.ru> 54.0.1-alt1
- New version (54.0.1).

* Mon May 08 2017 Alexey Gladkov <legion@altlinux.ru> 53.0.2-alt1
- New version (53.0.2).

* Mon Mar 20 2017 Alexey Gladkov <legion@altlinux.ru> 52.0-alt1
- New version (52.0).

* Tue Jan 31 2017 Alexey Gladkov <legion@altlinux.ru> 51.0.1-alt1
- New version (51.0.1).

* Thu Nov 17 2016 Alexey Gladkov <legion@altlinux.ru> 50.0-alt1
- New version (50.0).

* Thu Sep 29 2016 Alexey Gladkov <legion@altlinux.ru> 49.0.1-alt1
- New version (49.0.1).

* Wed Aug 10 2016 Alexey Gladkov <legion@altlinux.ru> 48.0-alt1
- New version (48.0).

* Tue Jun 21 2016 Alexey Gladkov <legion@altlinux.ru> 47.0-alt1
- New version (47.0).

* Sun May 01 2016 Alexey Gladkov <legion@altlinux.ru> 46.0-alt1
- New version (46.0).

* Tue Mar 22 2016 Alexey Gladkov <legion@altlinux.ru> 45.0.1-alt1
- New version (45.0.1).

* Thu Jan 28 2016 Alexey Gladkov <legion@altlinux.ru> 44.0-alt1
- New version (44.0).

* Thu Dec 24 2015 Alexey Gladkov <legion@altlinux.ru> 43.0.1-alt1
- New version (43.0.1).

* Tue Nov 10 2015 Alexey Gladkov <legion@altlinux.ru> 42.0-alt1
- New version (42.0).

* Tue Sep 29 2015 Alexey Gladkov <legion@altlinux.ru> 41.0-alt1
- New version (41.0).

* Mon Aug 17 2015 Alexey Gladkov <legion@altlinux.ru> 40.0.2-alt1
- New version (40.0.2).

* Mon Aug 10 2015 Alexey Gladkov <legion@altlinux.ru> 39.0.3-alt1
- New version (39.0.3).

* Mon May 25 2015 Alexey Gladkov <legion@altlinux.ru> 38.0.1-alt1
- New version (38.0.1).

* Thu Apr 09 2015 Alexey Gladkov <legion@altlinux.ru> 37.0.1-alt1
- New version (37.0.1).

* Mon Mar 09 2015 Alexey Gladkov <legion@altlinux.ru> 36.0.1-alt1
- New version (36.0.1).

* Tue Jan 27 2015 Alexey Gladkov <legion@altlinux.ru> 35.0-alt1
- New version (35.0).

* Tue Dec 09 2014 Alexey Gladkov <legion@altlinux.ru> 34.0-alt1
- New version (34.0).

* Fri Oct 24 2014 Alexey Gladkov <legion@altlinux.ru> 33.0-alt1
- New version (33.0).

* Wed Oct 01 2014 Alexey Gladkov <legion@altlinux.ru> 32.0-alt1
- New version (32.0).

* Wed Jul 30 2014 Alexey Gladkov <legion@altlinux.ru> 31.0-alt1
- New version (31.0).

* Sun May 11 2014 Alexey Gladkov <legion@altlinux.ru> 29.0.1-alt1
- New version (29.0.1).

* Thu Mar 27 2014 Alexey Gladkov <legion@altlinux.ru> 28.0-alt1
- New version (28.0).

* Fri Feb 14 2014 Alexey Gladkov <legion@altlinux.ru> 27.0-alt1
- New version (27.0).

* Sat Dec 28 2013 Alexey Gladkov <legion@altlinux.ru> 26.0-alt1
- New version (26.0).

* Wed Nov 06 2013 Alexey Gladkov <legion@altlinux.ru> 25.0-alt1
- New version (25.0).

* Fri Oct 25 2013 Alexey Gladkov <legion@altlinux.ru> 24.0-alt1
- New version (24.0).

* Wed Aug 14 2013 Alexey Gladkov <legion@altlinux.ru> 23.0-alt1
- New version (23.0).

* Mon Jul 01 2013 Alexey Gladkov <legion@altlinux.ru> 22.0-alt1
- New version (22.0).

* Tue Jun 18 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt2
- Add dictionary extension (ALT#29063).

* Wed Jun 05 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt1
- New version (21.0)

* Mon Apr 15 2013 Alexey Gladkov <legion@altlinux.ru> 20.0-alt1
- New version (20.0)

* Wed Mar 06 2013 Alexey Gladkov <legion@altlinux.ru> 19.0.1-alt1
- New version (19.0.1).

* Fri Jan 18 2013 Alexey Gladkov <legion@altlinux.ru> 18.0-alt1
- New version (18.0).

* Sun Nov 25 2012 Alexey Gladkov <legion@altlinux.ru> 17.0-alt1
- New version (17.0).

* Mon Oct 29 2012 Alexey Gladkov <legion@altlinux.ru> 16.0.1-alt1
- New version (16.0.1).

* Sun Sep 02 2012 Alexey Gladkov <legion@altlinux.ru> 15.0-alt1
- New version (15.0).

* Sun Aug 05 2012 Alexey Gladkov <legion@altlinux.ru> 14.0.1-alt1
- New version (14.0.1).

* Tue Jul 10 2012 Alexey Gladkov <legion@altlinux.ru> 13.0.1-alt1
- New version (13.0.1).

* Tue May 08 2012 Alexey Gladkov <legion@altlinux.ru> 12.0-alt1
- new version (12.0).

* Wed Apr 25 2012 Alexey Gladkov <legion@altlinux.ru> 11.0-alt1
- new version (11.0).

* Sun Feb 26 2012 Alexey Gladkov <legion@altlinux.ru> 10.0.2-alt1
- new version (10.0.2).

* Wed Jan 18 2012 Alexey Gladkov <legion@altlinux.ru> 9.0.1-alt1
- new version (9.0.1).

* Tue Nov 22 2011 Alexey Gladkov <legion@altlinux.ru> 8.0-alt1
- new version (8.0).

* Thu Oct 13 2011 Alexey Gladkov <legion@altlinux.ru> 7.0.1-alt1
- new version (7.0.1).

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.2-alt1
- new version (6.0.2).

* Fri Aug 26 2011 Alexey Gladkov <legion@altlinux.ru> 6.0-alt1
- new version (6.0).

* Mon Aug 01 2011 Alexey Gladkov <legion@altlinux.ru> 5.0.1-alt1
- new version (5.0.1).

* Sun Apr 17 2011 Alexey Gladkov <legion@altlinux.ru> 4.0-alt1
- new version (4.0).

* Tue Feb 02 2010 Alexey Gladkov <legion@altlinux.ru> 3.6-alt1
- new version (3.6).

* Thu Jul 30 2009 Michael Shigorin <mike@altlinux.org> 3.5.1-alt2
- rebuilt for Sisyphus (gear repo again)

* Wed Jul 22 2009 Led <led@altlinux.ru> 3.5.1-alt1
- 3.5.1
- cleaned up spec
- fixed License

* Sun Jul 05 2009 Led <led@altlinux.ru> 3.5-alt1
- 3.5

* Tue Mar 17 2009 Alexey Gladkov <legion@altlinux.ru> 3.1-alt2
- Fix max/min version in install.rdf.

* Tue Mar 10 2009 Alexey Gladkov <legion@altlinux.ru> 3.1-alt1
- new version (3.1).

* Wed Jul 16 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt2
- Bugfix version.
- Use dictionaries from hunspell-uk.

* Mon Jul 07 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1
- new version (3.0).

* Sun Mar 18 2007 L.A. Kostis <lakostis@altlinux.ru> 2.0-alt1
- new version for 2.0.0.*
- update .spec for new rpm-build-firefox.
- update CID.

* Wed Sep 27 2006 L.A. Kostis <lakostis@altlinux.ru> 1.5.0.7-alt1
- rebuild for Firefox 1.5.0.7.

* Thu Aug 10 2006 L.A. Kostis <lakostis@altlinux.ru> 1.5.0.6-alt1
- rebuild for Firefox 1.5.0.6.

* Thu Jun 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.4-alt1
- rebuild with firefox 1.5.0.4

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.3-alt1
- NMU: rebuild with firefox 1.5.0.3

* Sat Jan 07 2006 LAKostis <lakostis at altlinux.ru> 1.5-alt1
- New version for new firefox.
- Rebuild using new rpm-build-firefox.

* Thu Nov 10 2005 Konstantin A Lepikhov (L.A. Kostis) <lakostis@altlinux.ru> 1.0.7-alt1.1
- rebuild with new firefox.

* Wed Oct 12 2005 LAKostis <lakostis at altlinux.ru> 1.0.7-alt1
- Rebuild with new firefox.

* Fri Aug 26 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1.3
- firefox after firefox-uk installation will be switched to uk_UA.
- postun script bugfix.

* Tue Aug 16 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1.2
- bugfix rebuild.

* Mon Aug 15 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1.1
- Rebuild with new firefox.

* Wed Jun 22 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt1
- First build for ALT Linux.
