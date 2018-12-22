Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.1
%global namedversion gl%{version}-android-2.1_r1
Name:          android-opengl-api
Version:       1.1
Release:       alt1_14jpp8
Summary:       Google Android Java ME Library (Khronos)
License:       Apache-2.0
# While the EULA for the Android SDK restricts distribution of those binaries, the source code 
# is licensed under Apache 2.0 which allows compiling binaries from source and then distributing
# those versions.
URL:           http://developer.android.com/guide/topics/graphics/opengl.html
Source0:       http://repo1.maven.org/maven2/org/khronos/opengl-api/%{namedversion}/opengl-api-%{namedversion}-sources.jar
Source1:       http://repo1.maven.org/maven2/org/khronos/opengl-api/%{namedversion}/opengl-api-%{namedversion}.pom
# android-opengl-api package don't include the license file    
Source2:       http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires: maven-local
BuildArch:     noarch
Source44: import.info

%description
The Android implementation of Khronos OpenGL Spec
for the Google Android SDK.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -T -q -c
mkdir -p src/main/java

(
  cd src/main/java
  jar -xf %{SOURCE0}
  rm -rf META-INF
)

cp -p %{SOURCE1} pom.xml

cp -p %{SOURCE2} .
sed -i 's/\r//' LICENSE-2.0.txt

%mvn_file :opengl-api opengl-api

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE-2.0.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_13jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_11jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_10jpp8
- new version

