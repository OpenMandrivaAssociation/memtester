%define name memtester
%define version 4.0.6
%define release %mkrel 3

Name: %{name}
Summary: Memtester is a memory tester
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Group: Monitoring
URL: http://www.pyropus.ca/software/memtester/
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL

%description
Memtest is a utility for testing the memory subsystem in a computer to
determine if it is faulty. The original source was by Simon Kirby
<sim@stormix.com>. I have by this time completely rewritten the
original source, and added many additional tests to help catch
borderline memory. I also rewrote the original tests (which catch
mainly memory bits which are stuck permanently high or low) so that
they run approximately an order of magnitude faster.     



%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
%make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 memtester $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 memtester.8 $RPM_BUILD_ROOT%{_mandir}/man8/

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc BUGS CHANGELOG COPYING README.tests README 
%{_bindir}/*
%{_mandir}/man8/*


