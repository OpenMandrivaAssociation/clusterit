%define name	clusterit
%define	version 2.4
%define release	%mkrel 4

Summary:	Collection of clustering tools
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		Networking/Remote access
URL:		http://clusterit.sourceforge.net/
Source:		%{name}-%{version}.tar.bz2
Source1:	dshbak.sh
Patch1:		Makefile.patch.bz2
BuildRequires:  X11-devel
Requires:	openssh-clients, rsh, gawk
Provides:	%{name}-%{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}
Prefix:		%{_prefix}

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
rm -rf ${buildroot}
%setup -q
#%patch1 -p0

%build
install -m644 %{SOURCE1} $RPM_BUILD_DIR/%{name}-%{version}/tools/dshbak.sh
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root) 
%doc INSTALL CHANGES README html/*.html html/man/*.html
%{_mandir}/man1/*
%{_bindir}/*

