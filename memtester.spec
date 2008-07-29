Summary:	Memory tester
Name:		memtester
Version:	4.0.8
Release:	%mkrel 5
License:	GPL
Group:		Monitoring
URL:		http://www.pyropus.ca/software/memtester/
Source:		http://pyropus.ca/software/memtester/old-versions/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Memtest is a utility for testing the memory subsystem in a computer to
determine if it is faulty.

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
