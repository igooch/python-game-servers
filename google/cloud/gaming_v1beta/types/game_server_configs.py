# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.gaming_v1beta.types import common

__protobuf__ = proto.module(
    package="google.cloud.gaming.v1beta",
    manifest={
        "ListGameServerConfigsRequest",
        "ListGameServerConfigsResponse",
        "GetGameServerConfigRequest",
        "CreateGameServerConfigRequest",
        "DeleteGameServerConfigRequest",
        "ScalingConfig",
        "FleetConfig",
        "GameServerConfig",
    },
)


class ListGameServerConfigsRequest(proto.Message):
    r"""Request message for
    GameServerConfigsService.ListGameServerConfigs.

    Attributes:
        parent (str):
            Required. The parent resource name. Uses the form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/configs/*``.
        page_size (int):
            Optional. The maximum number of items to return. If
            unspecified, server will pick an appropriate default. Server
            may return fewer items than requested. A caller should only
            rely on response's
            [next_page_token][google.cloud.gaming.v1beta.ListGameServerConfigsResponse.next_page_token]
            to determine if there are more GameServerConfigs left to be
            queried.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request, if any.
        filter (str):
            Optional. The filter to apply to list
            results.
        order_by (str):
            Optional. Specifies the ordering of results following syntax
            at
            https://cloud.google.com/apis/design/design_patterns#sorting_order.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListGameServerConfigsResponse(proto.Message):
    r"""Response message for
    GameServerConfigsService.ListGameServerConfigs.

    Attributes:
        game_server_configs (MutableSequence[google.cloud.gaming_v1beta.types.GameServerConfig]):
            The list of game server configs.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            List of locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    game_server_configs: MutableSequence["GameServerConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GameServerConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class GetGameServerConfigRequest(proto.Message):
    r"""Request message for
    GameServerConfigsService.GetGameServerConfig.

    Attributes:
        name (str):
            Required. The name of the game server config to retrieve.
            Uses the form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/configs/{config}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateGameServerConfigRequest(proto.Message):
    r"""Request message for
    GameServerConfigsService.CreateGameServerConfig.

    Attributes:
        parent (str):
            Required. The parent resource name. Uses the form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/``.
        config_id (str):
            Required. The ID of the game server config
            resource to be created.
        game_server_config (google.cloud.gaming_v1beta.types.GameServerConfig):
            Required. The game server config resource to
            be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    game_server_config: "GameServerConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GameServerConfig",
    )


class DeleteGameServerConfigRequest(proto.Message):
    r"""Request message for
    GameServerConfigsService.DeleteGameServerConfig.

    Attributes:
        name (str):
            Required. The name of the game server config to delete. Uses
            the form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/configs/{config}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ScalingConfig(proto.Message):
    r"""Autoscaling config for an Agones fleet.

    Attributes:
        name (str):
            Required. The name of the Scaling Config
        fleet_autoscaler_spec (str):
            Required. Agones fleet autoscaler spec.
            Example spec:
            https://agones.dev/site/docs/reference/fleetautoscaler/
        selectors (MutableSequence[google.cloud.gaming_v1beta.types.LabelSelector]):
            Labels used to identify the game server
            clusters to which this Agones scaling config
            applies. A game server cluster is subject to
            this Agones scaling config if its labels match
            any of the selector entries.
        schedules (MutableSequence[google.cloud.gaming_v1beta.types.Schedule]):
            The schedules to which this Scaling Config
            applies.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fleet_autoscaler_spec: str = proto.Field(
        proto.STRING,
        number=2,
    )
    selectors: MutableSequence[common.LabelSelector] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=common.LabelSelector,
    )
    schedules: MutableSequence[common.Schedule] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=common.Schedule,
    )


class FleetConfig(proto.Message):
    r"""Fleet configs for Agones.

    Attributes:
        fleet_spec (str):
            Agones fleet spec. Example spec:
            ``https://agones.dev/site/docs/reference/fleet/``.
        name (str):
            The name of the FleetConfig.
    """

    fleet_spec: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GameServerConfig(proto.Message):
    r"""A game server config resource.

    Attributes:
        name (str):
            The resource name of the game server config. Uses the form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/configs/{config}``.
            For example,

            ``projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (MutableMapping[str, str]):
            The labels associated with this game server
            config. Each label is a key-value pair.
        fleet_configs (MutableSequence[google.cloud.gaming_v1beta.types.FleetConfig]):
            FleetConfig contains a list of Agones fleet
            specs. Only one FleetConfig is allowed.
        scaling_configs (MutableSequence[google.cloud.gaming_v1beta.types.ScalingConfig]):
            The autoscaling settings.
        description (str):
            The description of the game server config.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    fleet_configs: MutableSequence["FleetConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="FleetConfig",
    )
    scaling_configs: MutableSequence["ScalingConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="ScalingConfig",
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
