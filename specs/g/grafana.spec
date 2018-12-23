%global import_path github.com/grafana/grafana
%global commit d812109ebf3b904c9fcd8bc17f6d9b246232743b

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*


Name:		grafana
Version:	5.4.2
Release:	alt1
Summary:	Metrics dashboard and graph editor

Group:		Development/Other
License:	Apache-2.0
URL:		https://grafana.com

Source: %name-%version.tar
Patch: %name-%version.patch

Source100: %name-server.sysconfig
#Source101: %name.logrotate
Source102: %name-server.init
Source103: %name-server.service
Source104: %name.tmpfiles


#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64
BuildRequires(pre): rpm-build-golang rpm-build-ubt
BuildRequires: npm yarn
BuildRequires: node node-devel
BuildRequires: fontconfig libfreetype
BuildRequires: /proc

%add_verify_elf_skiplist %_datadir/%name/vendor/phantomjs/phantomjs

%description
Grafana is an open source, feature rich metrics dashboard and graph editor
for Graphite, Elasticsearch, OpenTSDB, Prometheus and InfluxDB.

%prep
# Build the Front-end Assets
# $ npm install yarn
# $ ./node_modules/.bin/yarn install --pure-lockfile
# $ npm run build
# $ git add -f node_modules
# $ git commit -n --no-post-rewrite -m "add node js modules"

%setup -q
%patch -p1

# add symlink to node headers
node_ver=$(node -v | sed -e "s/v//")
mkdir -p node_modules/.node-gyp/$node_ver/include
ln -s %_includedir/node node_modules/.node-gyp/$node_ver/include/node
echo "9" > node_modules/.node-gyp/$node_ver/installVersion

%build

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export npm_config_devdir="$PWD/node_modules/.node-gyp"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

%golang_build pkg/cmd/*
#go install -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" ./...

npm rebuild
npm run build

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"


pushd .gopath/src/%import_path
# Install Front-end Assets
install -d -m 755 %buildroot%_datadir/%name
cp -pr conf %buildroot%_datadir/%name/
cp -pr public %buildroot%_datadir/%name/
%golang_install
popd

rm -rf -- %buildroot/usr/src
rm -f -- %buildroot%_bindir/govendor

# Install config files
install -p -D -m 640 conf/sample.ini %buildroot%_sysconfdir/%name/%name.ini
install -p -D -m 640 conf/ldap.toml %buildroot%_sysconfdir/%name/ldap.toml
mkdir -p %buildroot%_sysconfdir/%name/provisioning/{dashboards,datasources}
install -p -D -m 640 conf/provisioning/dashboards/sample.yaml %buildroot%_sysconfdir/%name/provisioning/dashboards/sample.yaml
install -p -D -m 640 conf/provisioning/datasources/sample.yaml %buildroot%_sysconfdir/%name/provisioning/datasources/sample.yaml
# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 755 %buildroot%_sharedstatedir/%name
# Install pid directory
install -d -m 775 %buildroot%_runtimedir/%name
# Install sysconfig
install -p -D -m 644 %SOURCE100 %buildroot%_sysconfdir/sysconfig/%name-server
# Install logrotate
#install -p -D -m 644 %%SOURCE101 %buildroot%_logrotatedir/%name
# Install sysv init scripts
install -p -D -m 755 %SOURCE102 %buildroot%_initdir/%name-server
# Install systemd unit services
install -p -D -m 644 %SOURCE103 %buildroot%_unitdir/%name-server.service
install -p -D -m 644 %SOURCE104 %buildroot%_tmpfilesdir/%name.conf

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name  -c 'Grafana Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name-server

%preun
%preun_service %name-server

%files
%doc CHANGELOG.md LICENSE.md README.md
%_bindir/%name-cli
%_bindir/%name-server
%config(noreplace) %_sysconfdir/sysconfig/%name-server
%_initdir/%name-server
%_unitdir/%name-server.service
%_tmpfilesdir/%name.conf
%dir %attr(0750, root, %name) %_sysconfdir/%name
%dir %attr(0750, root, %name) %_sysconfdir/%name/provisioning
%dir %attr(0750, root, %name) %_sysconfdir/%name/provisioning/dashboards
%dir %attr(0750, root, %name) %_sysconfdir/%name/provisioning/datasources
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.ini
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/ldap.toml
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/provisioning/*/*.yaml
#%config(noreplace) %_logrotatedir/%name
%dir %attr(0770, root, %name) %_logdir/%name
%dir %attr(0775, root, %name) %_runtimedir/%name
%dir %attr(0755, %name, %name) %_sharedstatedir/%name
%_datadir/%name

%changelog
* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 5.4.2-alt1
- 5.4.2

* Mon Oct 15 2018 Alexey Shabalin <shaba@altlinux.org> 5.3.0-alt1
- 5.3.0

* Thu Jun 21 2018 Alexey Shabalin <shaba@altlinux.ru> 5.1.4-alt2%ubt
- update init script and systemd unit
- fix package files and config

* Wed Jun 20 2018 Alexey Shabalin <shaba@altlinux.ru> 5.1.4-alt1%ubt
- 5.1.4

* Wed Feb 14 2018 Alexey Shabalin <shaba@altlinux.ru> 4.6.3-alt1%ubt
- 4.6.3

* Mon Dec 04 2017 Alexey Shabalin <shaba@altlinux.ru> 4.6.2-alt1%ubt
- 4.6.2

* Mon Oct 30 2017 Alexey Shabalin <shaba@altlinux.ru> 4.6.0-alt1%ubt
- 4.6.0

* Fri Oct 13 2017 Alexey Shabalin <shaba@altlinux.ru> 4.5.2-alt1%ubt
- 4.5.2

* Mon Aug 28 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt2%ubt
- fix start options for systemd and sysvinit

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt1%ubt
- 4.4.3
- fix pidfile path in systemd unit
- fix run with sysv init script

* Tue Aug 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.2-alt1
- 4.4.2
- fix systemd unit
- rm phantomjs blob

* Thu Jul 27 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt2
- fix service name in post and preun

* Tue Jul 25 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt1
- First build for ALTLinux.
