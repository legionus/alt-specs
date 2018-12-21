Name: pysol-music
Version: 4.40
Release: alt2

Summary: PySol provides several solitaire card games
License: GPL
Group: Games/Cards
URL: http://www.oberhumer.com/opensource/pysol/

Source0: %name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pysol

%description
A collection of additional background music adapted for use with PySol.
I'm distributing this as its own package because I want to
keep the main distribution reasonable small.

%prep
%setup -q

%install
%__mkdir_p %buildroot%_gamesdatadir/pysol/music
pushd data/music
    cp * %buildroot%_gamesdatadir/pysol/music
popd

%files
%_gamesdatadir/pysol/music/*


%changelog
* Mon Oct 12 2009 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2
- moved to /usr/share/games (to fix the build)

* Thu Oct 30 2003 Alexei Takaseev <taf@altlinux.ru> 4.40-alt1
- initial package

