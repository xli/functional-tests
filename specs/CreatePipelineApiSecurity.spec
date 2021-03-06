// --GO-LICENSE-START--
// Copyright 2015 ThoughtWorks, Inc.
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//    http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// --GO-LICENSE-END--

CreatePipelineApiSecurity
=========================
// distributed under the License is distributed on an "AS IS" BASIS,

Setup of contexts
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1, pipeline2" - setup
* Capture go state "CreatePipelineApiSecurity" - setup

CreatePipelineApiSecurity
-------------------------

tags: 4141, group admin, api

The users in the system

Pipeline Groups - group 1
						  group 2

Role: group1AdminRole
Group Admins: group1Admin
Group Users: group1View

Admins: admin

* Logout - On Any Page

* Login as "group1Admin"

* For pipeline group "group1"
* Create pipeline "newpipeline" using template "simple-pass"

* Verify pipeline "newpipeline" is visible

* For pipeline group "group1"
* Delete pipeline "newpipeline" - Configure cruise using api

* Verify pipeline "newpipeline" is not visible

* For pipeline group "group2"
* As current User
* Create pipeline "newpipeline" using template "simple-pass"
* Response should return code "401"

* Logout - On Any Page

* Login as "group1View"

* For pipeline group "group1"
* Create pipeline "newpipeline" using template "simple-pass"
response should return code "401" (currently returning "403")





Teardown of contexts
____________________
* Capture go state "CreatePipelineApiSecurity" - teardown
* Using pipeline "pipeline1, pipeline2" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


