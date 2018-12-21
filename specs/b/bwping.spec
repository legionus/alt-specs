# -*- coding: latin-1; mode: rpm-spec -*-

Name: bwping
Version: 1.7
Release: alt2

Summary: Tool to measure bandwidth and response times between two hosts using Internet Control Message Protocol (ICMP)
License: BSD
Group: Monitoring
Url: bwping.sourceforge.net
Source: %name-%version.tar

Packager: Evgenii Terechkov <evg@altlinux.org>

%description
BWPing is a tool to measure bandwidth and response times between two
hosts using Internet Control Message Protocol (ICMP) echo request/echo
reply mechanism. It does not require any special software on the
remote host. The only requirement is the ability to respond on ICMP
echo request messages.

Although BWPing does not require any special software on the remote
host (only the ability to respond on ICMP echo request messages),
there are some special requirements to network infrastructure, local
and remote host performance:

- There should be no ICMP echo request/reply filtering on the network;
  this includes QoS mechanisms (which often affects ICMP) at any
  point in the testing path.

- Local host should have enough CPU resources to send ICMP echo
  request messages with given rate, and remote host should quickly
  respond on these messages and should have no ICMP bandwidth
  limiting turned on.

If some of these requirements are not satisfied then the measurement
results will be inadequate or fail completely. In general, for testing
bandwidth where QoS is implemented, always test with traffic that
matches the QoS class to be tested.

%prep
%setup
%build
sed -i 's|ac_cv_ipv6=no|ac_cv_ipv6=yes|g' configure
%configure
%make

%install
%makeinstall_std

%files
%_sbindir/%name
%_sbindir/%{name}6
%_man8dir/%{name}.8.*
%_man8dir/%{name}6.8.*

%changelog
* Thu Oct  9 2014 Terechkov Evgenii <evg@altlinux.org> 1.7-alt2
- Hack to build with IPv6 supoort

* Tue Oct  7 2014 Terechkov Evgenii <evg@altlinux.org> 1.7-alt1
- new version

* Tue Jun 14 2011 Terechkov Evgenii <evg@altlinux.org> 1.4-alt1
- Initial build for ALT Linux Sisyphus
