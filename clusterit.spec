Summary:	Collection of clustering tools
Name:		clusterit
Version:	2.5
Release:	%mkrel 3
License:	BSD
Group:		Networking/Remote access
URL:		http://clusterit.sourceforge.net/
Source:		%{name}-%{version}.tar.gz
BuildRequires:  libx11-devel
BuildRequires:	ncurses-devel
Requires:	openssh-clients, rsh, gawk
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a collection of clustering tools, to turn your ordinary 
everyday pile of UNIX workstations into a speedy parallel beast.
dsh : run a command on a cluster of machines.  dshbak : format the 
output of dsh. barrier, barrierd : synchronize a process on a number 
of machines. jsd : simple command scheduling daemon for remote execution. 
jsh : run scheduled commands on remote machines. run : run a command 
on a machine at random. seq : run a command on a cluster in sequence. 
pcp : copy a file to a cluster of machines. pdf : display free disk space
across a group of machines. prm : delete a file or files on a cluster 
of machines. rvt : a specialized VT100 emulator for the X window system. 
dvt : clustersed quickly dissect cluster files.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root) 
%doc INSTALL CHANGES README html/*.html html/man/*.html
%{_mandir}/man1/*
%{_bindir}/*


%changelog
* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 2.5-3mdv2011.0
+ Revision: 633698
- invalid source
- patch is of no use
- bunzip2 the patch

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

  + Sandro Cazzaniga <kharec@mandriva.org>
    - fix %%build to use %%make
    - use %%make
    - very little spec cleanup
    - new version 2.5, use %%configure2_5x and a tar.gz file

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 2.4-5mdv2010.0
+ Revision: 424881
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.4-4mdv2009.0
+ Revision: 243532
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.4-2mdv2008.1
+ Revision: 170786
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.4-1mdv2008.1
+ Revision: 123242
- kill re-definition of %%buildroot on Pixel's request
- import clusterit


* Fri Apr 28 2006 Jerome Soyer <saispo@mandriva.org> 2.4-1mdk
- New release 2.4
- Fix Url

* Fri Sep 09 2005 Antoine Ginies <aginies@mandrakesoft.com> 2.3.1-2mdk
- Fix BuildRquires

* Fri Jul 22 2005 Erwan Velu <velu@seanodes.com> 2.3.1-1mdk
- 2.3.1

* Wed May 19 2004 Antoine Ginies <aginies@n2.mandrakesoft.com> 2.2-1mdk
- release 2.2
* Fri Jan 03 2003 Antoine Ginies <aginies@mandrakesoft.com> 2.0-6mdk
- build for new glibc 
* Tue Aug 6 2002 Antoine Ginies <aginies@mandrakesoft.com> 2.0-5mdk
- build with gcc 3.2
* Thu Jul 11 2002 Antoine Ginies <aginies@mandrakesoft.com> 2.0-4mdk
- Build on 8.2 with 2.96
* Wed Jul 03 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.0-3mdk
- fix ~rpm/... pb
* Fri May 17 2002 Antoine Ginies <aginies@mandrakesoft.com> 2.0-2mdk 
- solve conflict problem with sh-utils
- correct stupid error of changelog
* Tue Apr 30 2002 Antoine Ginies <aginies@mandrakesoft.com> 2.0-1mdk
- first release for Mandrakesoft :-)
