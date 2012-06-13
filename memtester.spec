Summary:	Memory tester
Name:		memtester
Version:	4.3.0
Release:	1
License:	GPLv2
Group:		Monitoring
URL:		http://pyropus.ca/software/memtester/
Source0:	http://pyropus.ca/software/memtester/old-versions/%{name}-%{version}.tar.gz

%description
Memtest is a utility for testing the memory subsystem in a computer to
determine if it is faulty.

%prep
%setup -q

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 memtester %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man8
install -m 644 memtester.8 %{buildroot}%{_mandir}/man8/

%files
%doc BUGS CHANGELOG COPYING README.tests README
%{_bindir}/*
%{_mandir}/man8/*
