import argparse
import yaml
import json

parser = argparse.ArgumentParser(
    description="Preparation of values file to deploy a kubernetes service."
)

parser.add_argument(
    "--service-name",
    dest="service_name",
    help="The name of the service to deploy"
)

parser.add_argument(
    "--service-replica-count",
    type=int,
    dest="replica_count",
    help="The number of replicas of the service to deploy"
)

parser.add_argument(
    "--image-name",
    dest="image_name",
    help="The name of the image to deploy"
)

parser.add_argument(
    "--image-namespace",
    dest="image_namespace",
    help="The namespace of the image to deploy"
)

parser.add_argument(
    "--version",
    dest="version",
    help='The version of the application to deploy'
)

parser.add_argument(
    "--service-envvars",
    dest="service_envvars",
    help='The environment variables that are deployed with the service'
)

args = parser.parse_args()

values = {"service": {"name": args.service_name, "replicaCount": args.replica_count, "image": {"name": args.image_name, "namespace": args.image_namespace}, "env": json.loads(args.service_envvars)}}

with open("/service/values.yaml", "w") as output_file:
    yaml.dump(values, output_file)

with open("/service/Chart.yaml", "r+") as chart_file:
    yaml_file = yaml.full_load(chart_file)
    yaml_file["appVersion"] = args.version
    yaml_file["version"] = args.version
    chart_file.seek(0)
    chart_file.truncate()
    yaml.dump(yaml_file, chart_file)
