%define oldname jsmath-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Summary: A collection of Math symbol fonts 
Name:	 fonts-ttf-jsmath
Version: 20090708 
Release: alt3_12

# derived from computer modern metafont tex sources
License: Public domain 
Group: 	 System/Fonts/True type
Url: 	 http://www.math.union.edu/~dpvc/jsmath/welcome.html
Source0: http://www.math.union.edu/~dpvc/jsmath/download/TeX-fonts-linux.tgz
BuildArch: noarch

BuildRequires: fontpackages-devel
Source44: import.info

%description
%{summary}.


%prep

%setup -q -n TeX-fonts-linux 


%build


%install

# fonts
mkdir -p %{buildroot}%{_fontdir}
install -p -m644 *.ttf %{buildroot}%{_fontdir}/
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi


%files
%{_fontbasedir}/*/%{_fontstem}/*.ttf


%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 20090708-alt3_12
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20090708-alt3_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20090708-alt3_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20090708-alt3_5
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090708-alt3_4
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090708-alt2_4
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20090708-alt2_3
- rebuild with new rpm-build-fonts

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 20090708-alt1_3
- initial release by fcimport

