from importlib import resources as pkg_resource
import json

def main():
    p = pkg_resource.read_text("me.personal.module-usage.schema","neustar_contact_info.txt")
    print(p)

    q = pkg_resource.read_text("me.personal.module-usage.schema" , "cl_real_estate_schema.json")
    print(q)

    r = json.loads(pkg_resource.read_text("me.personal.module-usage.schema" , "cl_real_estate_schema.json"))
    print(r)
    print(r["quiz"])
    print(r["quiz"]["sport"])
    print(r["quiz"]["sport"]["q1"])
    print(r["quiz"]["sport"]["q1"]["question"])
    print(r["quiz"]["sport"]["q1"]["options"])
    print(r["quiz"]["sport"]["q1"]["options"][0])
    print(r["quiz"]["sport"]["q1"]["answer"])
    print(r["quiz"]["maths"])
    print(r["quiz"]["maths"]["q1"])
    print(r["quiz"]["maths"]["q1"]["question"])
    print(r["quiz"]["maths"]["q1"]["options"])
    print(r["quiz"]["maths"]["q1"]["options"][0] , r["quiz"]["maths"]["q1"]["options"][1] )
    print(r["quiz"]["maths"]["q1"]["answer"])
    print(r["quiz"]["maths"]["q2"])
    print(r["quiz"]["maths"]["q2"]["question"])
    print(r["quiz"]["maths"]["q2"]["options"])
    print(r["quiz"]["maths"]["q2"]["options"][0], r["quiz"]["maths"]["q2"]["options"][1])
    print(r["quiz"]["maths"]["q2"]["answer"])


if __name__ == "__main__":
    main()

