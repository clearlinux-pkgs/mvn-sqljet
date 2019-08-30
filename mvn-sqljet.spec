#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-sqljet
Version  : 1.1.10
Release  : 2
URL      : https://repo1.maven.org/maven2/org/tmatesoft/sqljet/sqljet/1.1.10/sqljet-1.1.10.jar
Source0  : https://repo1.maven.org/maven2/org/tmatesoft/sqljet/sqljet/1.1.10/sqljet-1.1.10.jar
Source1  : https://repo1.maven.org/maven2/org/tmatesoft/sqljet/sqljet/1.1.10/sqljet-1.1.10.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mvn-sqljet-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-sqljet package.
Group: Data

%description data
data components for the mvn-sqljet package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tmatesoft/sqljet/sqljet/1.1.10
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/tmatesoft/sqljet/sqljet/1.1.10

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tmatesoft/sqljet/sqljet/1.1.10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/tmatesoft/sqljet/sqljet/1.1.10


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/tmatesoft/sqljet/sqljet/1.1.10/sqljet-1.1.10.jar
/usr/share/java/.m2/repository/org/tmatesoft/sqljet/sqljet/1.1.10/sqljet-1.1.10.pom
