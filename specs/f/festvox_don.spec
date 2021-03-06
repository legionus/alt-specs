%define voice don
%define voicepath english/don_diphone
%define version	1.95
%define release	alt2

Name:		festvox_%{voice}
Version:	%{version}
Release:	%{release}
Group:		Sound
Copyright:	X11-style
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voice: British English RP male speaker (low quality)
Requires:	festival, festlex_POSLEX, festlex_OALD
Provides:	festvox
BuildArch:	noarch
# useless and too slow on large data files
AutoReqProv:	no

Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festvox_%{voice}.tar.gz

%description
   British English RP male speaker using spike excited LPC diphone
   database, small database give poorer quality but runs fast.

%prep
%setup -q -c

%build

%install
VOICE_DIR=$RPM_BUILD_ROOT%{_datadir}/festival/voices

install -d $VOICE_DIR/%{voicepath}/festvox
#install -d $VOICE_DIR/%{voicepath}/group
install -m 644 festival/lib/voices/%{voicepath}/festvox/* $VOICE_DIR/%{voicepath}/festvox
#install -m 644 festival/lib/voices/%{voicepath}/group/* $VOICE_DIR/%{voicepath}/group
install -m 644 festival/lib/voices/%{voicepath}/*.* $VOICE_DIR/%{voicepath}/

%files
%doc festival/lib/voices/%{voicepath}/COPYING
%{_datadir}/festival/*

%changelog
* Wed Oct 18 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt2
- fixed dependency on OALD

* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- initial release for Sisyphus
