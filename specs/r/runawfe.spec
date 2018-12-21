Name: runawfe
Version: 4.3.0
Release: alt15

Summary: Runawfe

License: LGPL
Group: Office
Url: http://sourceforge.net/projects/runawfe/

Source: %name-%version.tar
Source1: standalone-runa.xml
Source2: runawfe-server
Source3: wildfly-as-runawfe-server.conf
Source4: runawfe-server.service
Source5: runawfe-server-start.desktop
Source6: runawfe-server.png
Source7: runawfe-server-stop.desktop
Source8: runawfe-notifier.desktop
Source9: runawfe-notifier.png
Source10: runawfe-gpd.desktop
Source11: runawfe-gpd.png

Packager: Danil Mikhailov <danil@altlinux.org>

#PreReq:
Requires: wildfly-as >= 10.1.0-alt1
#Provides:
#Conflicts:

#BuildPreReq:
# Automatically added by buildreq on Fri Sep 06 2013
# optimized out: apache-commons-cli atinject google-guice guava java java-devel jpackage-utils maven maven-wagon nekohtml plexus-cipher plexus-classworlds plexus-containers-component-annotations plexus-interpolation plexus-sec-dispatcher plexus-utils python3-base sisu tzdata tzdata-java xbean xerces-j2 xml-commons-jaxp-1.4-apis
AutoReq: yes,noperl,nopython
BuildPreReq: rpm-build-java java-devel-default

BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-deploy-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-ejb-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-war-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-ear-plugin)
BuildRequires: chrpath
BuildRequires: wildfly-as

%define wildflyuser wildfly-as
%define runauser _runa
%define runadir /var/lib/%name
%define runagpddir %_libdir/runawfe-gpd
%define runartndir /var/lib/runawfe-notifier
%define wildflydir %_datadir/wildfly-as/standalone
%define distrname ALTLinux

#Define for Fedora build http://forums.fedoraforum.org/showthread.php?t=182293
%define debug_package %{nil}

%define gpd_path gpd_source/plugins/ru.runa.gpd.maven/target/products/RunaWFE_DeveloperStudio/linux/gtk

#gpd copy path for multi arch
%ifarch x86_64
%define gpd_path_arch %{gpd_path}/x86_64/
%else
%define gpd_path_arch %{gpd_path}/x86/
%endif

%description
RunaWFE is a free OpenSource business process management system. It is delivered
under LGPL licence. RunaWFE is based on wildfly jBPM and Activiti. It provides rich
web interface with tasklist, form player, graphical process designer, bots and more.

%package server
Summary: Runawfe server
Requires: wildfly-as >= 10.1.0-alt1 gksu
License: LGPL
Group: Office
Url: http://sourceforge.net/projects/runawfe/
BuildArch: noarch

%description server
RunaWFE is a free OpenSource business process management system. It is delivered
under LGPL licence. RunaWFE is based on wildfly jBPM and Activiti. It provides rich
web interface with tasklist, form player, graphical process designer, bots and more.

%package gpd
Summary: Runawfe Graphic Process Designer
Requires: java >= 1.7, libwebkitgtk2
License: LGPL
Group: Office
Url: http://sourceforge.net/projects/runawfe/
Provides: osgi(ru.runa.gpd.form.ftl)

%description gpd
RunaWFE is a free OpenSource business process management system. It is delivered
under LGPL licence. RunaWFE is based on wildfly jBPM and Activiti. It provides rich
web interface with tasklist, form player, graphical process designer, bots and more.

%package notifier
Summary: Runawfe notifier client
Requires: java libwebkitgtk2
License: LGPL
Group: Office
Url: http://sourceforge.net/projects/runawfe/

%description notifier
RunaWFE is a free OpenSource business process management system. It is delivered
under LGPL licence. RunaWFE is based on wildfly jBPM and Activiti. It provides rich
web interface with tasklist, form player, graphical process designer, bots and more.

%prep
%setup

%build

export MAVEN_OPTS="-Dmaven.repo.local=$(pwd)/.m2/repository/"

# server
pushd .
cd wfe

cd wfe-app/repository/
./add_dependencies.sh
cd ..

%if %distrname == "Ubuntu" ||  %distrname == "Debian"
mvn clean package -Dappserver=jboss7
%else
%mvn_build -f -- -X -Dappserver=jboss7
%endif

popd 
# notifier
pushd .
cd notifier

xmvn install:install-file -Dfile=wfe-webservice-client.jar -DartifactId=wfe-webservice-client -DgroupId=ru.runa.wfe -Dversion=4.3.0-SNAPSHOT -Dpackaging=jar -DgeneratePom=true
xmvn package

popd

%install
# server
pushd .
cd wfe
mkdir -p %buildroot/%wildflydir/{bin,data,deployments,log,tmp,configuration}
mkdir -p %buildroot/etc/wildfly-as/
mkdir -p %buildroot/lib/systemd/system/
mkdir -p %buildroot%_desktopdir/
mkdir -p %buildroot%_pixmapsdir/

#FIX correct path to wildfly-as/bin
cp %SOURCE1 %buildroot%wildflydir/configuration/
cp %SOURCE3 %buildroot/etc/wildfly-as/
#cp %SOURCE4 %buildroot/lib/systemd/system/
cp %SOURCE5 %buildroot%_desktopdir/
cp %SOURCE6 %buildroot%_pixmapsdir/
cp %SOURCE7 %buildroot%_desktopdir/

mkdir -p %buildroot/%_sbindir/
mkdir -p %buildroot%_initdir/

%if %distrname == "Ubuntu" ||  %distrname == "Debian"

# Explain of server execution on:
# 1) deb we can runs like:
#  -  a program from bin dir
#  -  a very simple service - start is executing bin in a background (because we havent /etc/init.d/functions on this)
# 2) AltLinux and Fedora runs like:
#  -  a program (runs service start)
#  -  full supported service (starts wildfly with runa config)

cat >%buildroot/%_sbindir/%name <<EOF
#!/bin/sh
JBOSS_BASE_DIR=%wildflydir su - wildfly-as -s /bin/sh -c "/usr/share/wildfly-as/bin/standalone.sh -c standalone-runa.xml"

EOF

cat >%buildroot%_initdir/%name <<EOF
#!/bin/sh
if [ "\$1" = "start" ] ; then
    #rm -f %_runtimedir/%name.pid
    #ln -s %_runtimedir/wildfly-as/wildfly-as-standalone.pid %_runtimedir/%name.pid
    #TODO BUG not work macros %_runtimedir !
    %_sbindir/%name > /var/log/%name 2>&1 &
fi
if [ "\$1" = "stop" ] ; then
    %wildflydir/../bin/jboss-cli.sh --connect --command=:shutdown
    #/usr/share/wildfly-as/bin/
fi

EOF

%else

cat >%buildroot%_initdir/%name <<EOF

#
# %name - runawfe server
#
# chkconfig: 2345 99 1
# processname: runawfe
# config: /etc/runawfe
# pidfile: %_runtimedir/%name.pid
#
### BEGIN INIT INFO
# Provides: %name
# Default-Start: 2 3 4 5
# Short-Description: runawfe server
# Description: runawfe server or botstation daemon
### END INIT INFO

rm -f %_runtimedir/%name.pid
ln -s %_runtimedir/wildfly-as/wildfly-as-standalone.pid %_runtimedir/%name.pid

export JBOSS_CONF=/etc/wildfly-as/wildfly-as-%name-server.conf

%_initdir/wildfly-as-standalone "\$1"

EOF

cat >%buildroot/%_sbindir/%name <<EOF
#!/bin/sh
%_initdir/%name "start"

EOF

%endif


cat >%buildroot/lib/systemd/system/%name.service <<EOF

[Unit]
Description=RunaWFE server daemon

[Service]
Type=simple
ExecStart=/usr/sbin/%name
PIDFile=%_runtimedir/%name.pid

EOF

cp -a wfe-ear/target/runawfe.ear %buildroot/%wildflydir/deployments/

popd
# notifier
pushd .
cd notifier

mkdir -p %buildroot/%runartndir/
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot%_pixmapsdir/
mkdir -p %buildroot%_desktopdir/

cp %SOURCE8 %buildroot%_desktopdir/
cp %SOURCE9 %buildroot/usr/share/pixmaps/

cat >%buildroot/%_bindir/runawfe-notifier <<EOF
cd %runartndir/
java -Dorg.eclipse.swt.browser.UseWebKitGTK=true -cp ".:rtn.jar:swt-gtk.jar" ru.runa.notifier.PlatformLoader
EOF

mkdir -p %buildroot/var/log/runawfe-notifier/
touch %buildroot/var/log/runawfe-notifier/rtn.log
ln -s /var/log/runawfe-notifier/rtn.log %buildroot/%runartndir/rtn.log


%if %distrname == "Debian"
#removed special version for debian
%define rtn_path target/rtn
%else
%define rtn_path target/rtn
%endif

#gpd copy path for multi arch
%define rtn_path_arch %{rtn_path}.jar

#in notifier/ dir
cp %rtn_path_arch %buildroot/%runartndir/rtn.jar

#onAppShutdown.wav  onAppStart.wav  onNewTask.wav  unreadTasksNotification.wav
cp target/classes/*.wav %buildroot/%runartndir/

popd
# gpd
pushd .

mkdir -p %buildroot/%runagpddir/
mkdir -p %buildroot%_pixmapsdir/
mkdir -p %buildroot%_desktopdir/

#in gpd/ dir
cp %SOURCE10 %buildroot%_desktopdir/
cp %SOURCE11 %buildroot%_pixmapsdir/
#cp -a ./* %buildroot/%runagpddir/ #default gpd copy path for x86 arch

mv %gpd_path_arch/runa-gpd %gpd_path_arch/runawfe-gpd
chmod 755 %gpd_path_arch/runawfe-gpd
#chrpath -d %gpd_path_arch/libcairo-swt.so
cp -a %gpd_path_arch/* %buildroot/%runagpddir/
cp -a gpd_source/workspace/ %buildroot/%runagpddir/

mkdir -p %buildroot/%_bindir/
cat >%buildroot/%_bindir/runawfe-gpd <<EOF
#!/bin/sh
gpddir="\$HOME/runawfe-gpd"

if [ ! -e ""\$gpddir/"" ] ; then
    gpdconfdir="\$HOME/runawfe-gpd/workspace/.metadata/.plugins/org.eclipse.core.runtime/.settings"
    gpdconf="\$gpdconfdir/ru.runa.gpd.prefs"
    mkdir -p "\$gpddir"
    mkdir -p \$gpdconfdir
    cp -na %runagpddir/workspace/ "\$gpddir/"
    chown -R \$USER "\$gpddir/"/workspace/
    find "\$gpddir/" -exec touch -t 201001010000 \{\} \\;
fi

cd "\$gpddir"
%runagpddir/runawfe-gpd

EOF

popd

%pre server
useradd -d %runadir -r -s %_sbindir/%name %runauser >/dev/null 2>&1 || :

%files server
/etc/wildfly-as/wildfly-as-runawfe-server.conf
%_pixmapsdir/*server*.*
%_desktopdir/*server*.*
%attr(755,%wildflyuser,root) %wildflydir/configuration/*
%attr(755,%wildflyuser,root) %wildflydir/deployments/*
%attr(755,root,root) %_sbindir/%name
%attr(755,root,root) %_initdir/%name
%attr(644,root,root) /lib/systemd/system/%name.service

%files gpd
%attr(755,root,root) %dir %runagpddir/
%runagpddir/*
%_pixmapsdir/*gpd.*
%_desktopdir/*gpd.*
%attr(755,root,root) %_bindir/runawfe-gpd
#%attr(755,root,root) %runagpddir/workspace/

%files notifier
%attr(755,%runauser,root) %dir %runartndir/
%_pixmapsdir/*notifier.*
%_desktopdir/*notifier.*
/var/log/runawfe-notifier/*
%runartndir/*
%attr(766,root,root) /var/log/runawfe-notifier/rtn.log
%attr(755,root,root) %_bindir/runawfe-notifier

%changelog
* Fri May 18 2018 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt15
- rtn port

* Sat May 12 2018 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt14
- gpd workspace 

* Wed May 02 2018 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt13
- gpd workspace 

* Tue May 01 2018 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt12
- gpd workspace 

* Mon Apr 30 2018 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt11
- gpd workspace 

* Mon Apr 30 2018 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt10
- Added dependency

* Sun Apr 29 2018 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt9
- Some fixes 

* Mon Mar 05 2018 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt8
- Updated to 4.3.0 code and wildfly

* Mon Mar 05 2018 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt7
- Updated to 4.3.0 code and wildfly

* Mon Dec 18 2017 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt4
- Updated to 4.3.0 code 

* Sat Oct 07 2017 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt3
- Updated to 4.3.0 code 

* Sun Sep 17 2017 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt2
- Updated to 4.3.0 code 

* Sat Sep 16 2017 Konstantinov Aleksey <kana@altlinux.org> 4.3.0-alt1
- Updated to 4.3.0 code 
