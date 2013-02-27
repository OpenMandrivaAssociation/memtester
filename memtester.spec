Summary:	Memory tester
Name:		memtester
Version:	4.3.0
Release:	2
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


%changelog
* Wed Jun 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.3.0-1
+ Revision: 805383
- version update 4.3.0

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 4.2.1-1
+ Revision: 645306
- update to new version 4.2.1

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1.3-2mdv2011.0
+ Revision: 612848
- the mass rebuild of 2010.1 packages

* Tue Mar 02 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.1.3-1mdv2010.1
+ Revision: 513602
- Update to 4.1.3

* Sun Nov 29 2009 Jérôme Brenier <incubusss@mandriva.org> 4.1.2-1mdv2010.1
+ Revision: 471026
- new version 4.1.2
- fix license tag

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 4.0.8-7mdv2010.0
+ Revision: 439797
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 4.0.8-6mdv2009.1
+ Revision: 350233
- 2009.1 rebuild

  + Nicolas Vigier <nvigier@mandriva.com>
    - fix url

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 4.0.8-5mdv2009.0
+ Revision: 252310
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 4.0.8-3mdv2008.1
+ Revision: 170980
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Jan 04 2008 Thierry Vignaud <tv@mandriva.org> 4.0.8-2mdv2008.1
+ Revision: 145446
- fix description

* Fri Jan 04 2008 Jérôme Soyer <saispo@mandriva.org> 4.0.8-1mdv2008.1
+ Revision: 144995
- New release

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Erwan Velu <erwan@mandriva.org>
    - 4.0.8

* Tue May 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.0.7-1mdv2008.0
+ Revision: 29707
- new version
- spec file clean

* Thu May 10 2007 Lenny Cartier <lenny@mandriva.org> 4.0.6-3mdv2008.0
+ Revision: 26168
- Provides manpage

