Summary:	Memtester is a memory tester
Name:		memtester
Version:	4.0.8
Release:	%mkrel 1
License:	GPL
Group:		Monitoring
URL:		http://www.pyropus.ca/software/memtester/
Source:		http://pyropus.ca/software/memtester/old-versions/%{name}-%{version}.tar.bz2

%description
Memtest is a utility for testing the memory subsystem in a computer to
determine if it is faulty. The original source was by Simon Kirby
<sim@stormix.com>. I have by this time completely rewritten the
original source, and added many additional tests to help catch
borderline memory. I also rewrote the original tests (which catch
mainly memory bits which are stuck permanently high or low) so that
they run approximately an order of magnitude faster.     



%prep
rm -rf %{buildroot}

%setup -q

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 memtester %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man8
install -m 644 memtester.8 %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot} 

%files 
%defattr(-,root,root)
%doc BUGS CHANGELOG COPYING README.tests README 
%{_bindir}/*
%{_mandir}/man8/*
