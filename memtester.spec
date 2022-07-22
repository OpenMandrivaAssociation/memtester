Summary:	Memory tester
Name:		memtester
Version:	4.5.1
Release:	1
License:	GPLv2+
Group:		Monitoring
Url:		http://pyropus.ca/software/memtester/
Source0:	http://pyropus.ca/software/memtester/old-versions/%{name}-%{version}.tar.gz

%description
Memtest is a utility for testing the memory subsystem in a computer to
determine if it is faulty.

%files
%doc BUGS CHANGELOG COPYING README.tests README
%{_bindir}/*
%{_mandir}/man8/*

#----------------------------------------------------------------------------

%prep
%setup -q
echo "cc %{optflags} -DPOSIX -D_POSIX_C_SOURCE=200809L -D_FILE_OFFSET_BITS=64 -DTEST_NARROW_WRITES -c" > conf-cc
echo "cc %{ldflags}" > conf-ld

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 memtester %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man8
install -m 644 memtester.8 %{buildroot}%{_mandir}/man8/

