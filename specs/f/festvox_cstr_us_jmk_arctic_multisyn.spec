%define voice cstr_us_jmk_arctic_multisyn
%define voicepath english/%voice

Name:		festvox_%{voice}
Version:	1.0
Release:	alt2
Group:		Sound
Copyright:	X11-style
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voice: Canadian English Male speaker (JMK), multisyn
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox
BuildArch:	noarch

Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festvox_%{voice}-%{version}.tar.bz2
Patch0:		festvox_cstr_us_jmk_arctic_multisyn-festival-1.96-alt.patch


%description
Canadian English male speaker (JMK), using excited residual LPC
multisyn database.   (Note this is about 100MB)


%prep
%setup -q -c
TAR_VOICE_DIR=festival/lib/voices-multisyn
pushd $TAR_VOICE_DIR
%patch -p2 -b .to_delete
popd

find . -name '*.to_delete' -print -delete

%build

%install
VOICE_DIR=$RPM_BUILD_ROOT%{_datadir}/festival/voices
TAR_VOICE_DIR=festival/lib/voices-multisyn

install -d $VOICE_DIR/%{voicepath}/festvox
install -m 644 $TAR_VOICE_DIR/%{voicepath}/festvox/*.scm $VOICE_DIR/%{voicepath}/festvox
mv $TAR_VOICE_DIR/%{voicepath}/jmk $VOICE_DIR/%{voicepath}/

%files
%{_datadir}/festival/*

%changelog
* Tue Sep 09 2008 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2
- fix for festival 1.96

* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- initial release for Sisyphus
